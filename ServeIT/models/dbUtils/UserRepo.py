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
            print(user)
            # login the user
            # ...
        except Exception as e:
            return {
                'code' : -1,
                'message' : f'{e}'
            }
    @staticmethod
    def signup(username, idnumber, fname, lname, email, course, college, password, gender):
        cur = mysql.connection.cursor()

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
            cur.execute(f''' INSERT INTO `users`(`userID`, `username`, `idnumber`, `fname`, `lname`, `email`, `college`, `course`, `password`, `gender`) VALUES
                        ('','{username}','{idnumber}','{fname}','{lname}','{email}','{college}','{course}','{password}','{gender}')
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
    def get_fname(username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT fname FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def get_username(username):
        cur = mysql.connection.cursor()
        cur.execute("SELECT username FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def user_Photo(user_id, file):
    