### THIS IS WHERE YOU MANIPULATE USER DATA IN THE DATABASE ###
from ServeIT import mysql
import re

class UserRepo:

    @staticmethod
    def login(username, password):
        cur = mysql.connection.cursor()
        try:
            cur.execute(f'''
                        SELECT * FROM users
                        WHERE `username` = '{username}' AND `password` = '{password}'
                        ''')
            user = cur.fetchone()
            if user is None:
                return {
                    'code': -1,
                    'message': 'Invalid username or password'
                }
            user_id = user[0]
            return {
                'code': 0,
                'user_id': user_id
            }
        except Exception as e:
            return {
                'code' : -1,
                'message' : f'{e}'
            }

    @staticmethod
    def signup(username, idnumber, fname, lname, email, course, college, password, gender):
        cur = mysql.connection.cursor()
        # Retrieve the maximum value of the user_id column
        cur.execute("SELECT MAX(user_id) FROM users")
        result = cur.fetchone()
        max_user_id = result[0]

        # Extract the number part from the maximum user_id and increment it by 1
        if max_user_id:
            number_part = int(max_user_id.split("SCSD")[1]) + 1
        else:
            # If the services table is empty, start the user_id from 1
            number_part = 1

        # Generate the new service code
        user_id = "SDID" + str(number_part).zfill(4)

        # validate email
        if not re.match(r'^[\w.-]+@[\w.-]+(\.[\w.-]+)+$', email):
            return {'code': -1, 'message': 'Email is already taken'}
        # validate password
        if not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
            return {'code': -1, 'message': 'The password must be at least 8 characters long and can contain only letters, digits and special characters'}
        # check if username is already taken    
        cur.execute(f'SELECT * FROM users WHERE username = "{username}"')
        user = cur.fetchone()
        if user is not None:
            return {'code': -1, 'message': 'Username is already taken'}

        # insert new user into the database
        cur.execute(f'SELECT * FROM users WHERE email = "{email}"')
        user = cur.fetchone()
        if user is not None:
            return {'code': -1, 'message': 'Email is already taken'}
        try:
            cur.execute(f''' INSERT INTO `users`(`user_id`, `username`, `idnumber`, `fname`, `lname`, `email`, `college`, `course`, `password`, `gender`) VALUES
                        ('{user_id}','{username}','{idnumber}','{fname}','{lname}','{email}','{college}','{course}','{password}','{gender}')
                        ''')
            mysql.connection.commit()
            return {
                'code': 1,
                'message': 'Account created'
            }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }

    @staticmethod
    def get_fname(userID):
        cur = mysql.connection.cursor()
        cur.execute("SELECT fname FROM users WHERE user_id = %s", (userID,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None

#create a function to get the current user's fname and lname in mysql database
    @staticmethod
    def get_current_user_name(userID):
        cur =mysql.connection.cursor()
        cur.execute("SELECT fname, lname FROM users WHERE user_id = %s", (userID,))
        result = cur.fetchone()
        if result:
            return f"{result[0]} {result[1]}"
        else:
            return None

#create a function to get the current user's college in mysql database
    @staticmethod
    def get_current_user_college(userID):
        cur =mysql.connection.cursor()
        cur.execute("SELECT college FROM users WHERE user_id = %s", (userID,))
        result = cur.fetchone()
        if result:
            return f"{result[0]}"
        else:
            return None 

#create a function to get the current user's course in mysql database
    @staticmethod
    def get_current_user_course(userID):
        cur =mysql.connection.cursor()
        cur.execute("SELECT course FROM users WHERE user_id = %s", (userID,))
        result = cur.fetchone()
        if result:
            return f"{result[0]}"
        else:
            return None
    
#create a function to update the current user's photo in mysql database
    @staticmethod
    def updateImg(ImgUrl, ThumbUrl, userID):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    UPDATE users
                    SET ImgUrl='{ImgUrl}',
                        ThumbUrl='{ThumbUrl}'
                    WHERE user_id='{userID}'
                    ''')
        mysql.connection.commit()
        return

#create a function to retrieve all data from the current user in users table in mysql database
    @staticmethod
    def get_current_user(userID):
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE user_id = %s", (userID,))
        data = cur.fetchone()
        return data
            

#create a function to update the current user's fname and lname in mysql database
    @staticmethod
    def Updatename(fname, lname, userID):
        cur = mysql.connection.cursor()
        cur.execute(f'''
                    UPDATE users
                    SET fname='{fname}',
                        lname='{lname}'
                    WHERE user_id='{userID}'
                    ''')
        mysql.connection.commit()
        return