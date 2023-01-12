from ServeIT import mysql, s3, S3_BUCKET
import boto3


class Services:
    
    @staticmethod
    def add_request(userID, order_status, location):       
        service_code = Services.get_service_code()
        paymentID = Services.get_payment_code()
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT MAX(CAST(request_id AS CHAR)) FROM requests")
            result = cur.fetchone()
            if result:
                max_request_code = result[0]
                if max_request_code:
                    number_part = int(max_request_code.split("SDRQID")[1].lstrip('0')) + 1
                else:
                    number_part = 1
            else:
                number_part = 1
            request_id = "SDRQID" + str(number_part).zfill(4)
            cur.execute(f''' INSERT INTO `requests`
                        (`request_id`, `user_id`, `service_code`, `order_status`, `order_date`, `payment_id`, `location`)
                        VALUES ('{request_id}', '{userID}', '{service_code}', '{order_status}', NOW(), '{paymentID}', '{location}')''')
            mysql.connection.commit()
            print("REQUEST ADDED")
            return {
                'code': 1,
                'message': 'Request Added'
            }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }

    @staticmethod
    def get_service_code():
        cur = mysql.connection.cursor()
        query = f"SELECT MAX(service_code) FROM services"
        cur.execute(query)
        result = cur.fetchone()
        if result[0] is None:
            return 0
        return result[0]
            

#ADD PRINTING DATA TO DATABASE
    @staticmethod
    def add_printing(fileURL, num_copies, description):
        service_code = Services.get_service_code_name("SFPR")
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT MAX(CAST(print_id AS CHAR)) FROM service_print")
            result = cur.fetchone()
            if result:
                max_print_id = result[0]
                if max_print_id:
                    number_part = int(max_print_id.split("SDPR")[1].lstrip('0')) + 1
                else:
                    number_part = 1
            else:
                number_part = 1
            print_id = "SDPR" + str(number_part).zfill(4)
            cur.execute(f''' INSERT INTO `service_print`
                        (`print_id`, `service_code`,`file`, `number_of_copies`, `description` ) 
                        VALUES ('{print_id}','{service_code}', '{fileURL}', '{num_copies}', '{description}')''')
            mysql.connection.commit()
            print("PRINTING ADDED")
            return {
                'code': 1,
                'message': 'Printing Request Added'
            }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }
    @staticmethod
    def add_gcash(gcash_type, amount , description, phonenumber):
        service_code = Services.get_service_code_name("SFGC")
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT MAX(CAST(gcash_id AS CHAR)) FROM service_gcash")
            result = cur.fetchone()
            if result:
                max_gcash_id = result[0]
                if max_gcash_id:
                    number_part = int(max_gcash_id.split("SDGC")[1].lstrip('0')) + 1
                else:
                    number_part = 1
            else:
                number_part = 1
            gcash_id = "SDGC" + str(number_part).zfill(4)
            cur.execute(f''' INSERT INTO `service_gcash`
                        (`gcash_id`, `service_code`,`gcash_type`, `amount`, `description`, `phone_number`) 
                        VALUES ('{gcash_id}','{service_code}','{gcash_type}', '{amount}', '{phonenumber}', '{description}')''')
            mysql.connection.commit()
            print("Gcash ADDED")
            return {
                'code': 1,
                'message': 'Gcash Request Added'
            }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }

    @staticmethod
    def add_service(service_name):
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT MAX(CAST(service_code AS CHAR)) FROM services")
            result = cur.fetchone()
            if result:
                max_service_code = result[0]
                if max_service_code:
                    number_part = int(max_service_code.split("SDSC")[1].lstrip('0')) + 1
                else:
                    number_part = 1
            else:
                number_part = 1

            service_code = "SDSC" + str(number_part).zfill(4)
            service_name = f"SF{service_name}"

            cur.execute(f''' INSERT INTO `services`
                        (`service_code`, `service_name`)
                        VALUES ('{service_code}', '{service_name}')''')
            mysql.connection.commit()
            print(service_code, service_name, "SERVICES ADDED")
            return {
                'code': 1,
                'message': 'Services Added' }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }
    @staticmethod
    def get_service_code_name(service_name):
        cur = mysql.connection.cursor()
        query = f"SELECT MAX(service_code) FROM services WHERE service_name = '{service_name}'"
        cur.execute(query)
        result = cur.fetchone()
        if result[0] is None:
            return 0
        return result[0]

    @staticmethod
    def get_payment(MOP):
        cur = mysql.connection.cursor()
        cur.execute("SELECT MAX(CAST(payment_id AS CHAR)) FROM payments")
        result = cur.fetchone()
        if result:
            max_payment_id = result[0]
            if max_payment_id:
                number_part = int(max_payment_id.split("SDPY")[1].lstrip('0')) + 1
            else:
                number_part = 1
        else:
            number_part = 1
        payment_id = "SDPY" + str(number_part).zfill(4)
        cur.execute(f''' INSERT INTO `payments` 
                    (`payment_id`, `mode_of_payment`) 
                    VALUES ('{payment_id}', '{MOP}')''')
        mysql.connection.commit()
        print( payment_id, MOP, "PAYMENT ADDED")

    @staticmethod
    def get_payment_code():
        cur = mysql.connection.cursor()
        query = f"SELECT MAX(payment_id) FROM payments"
        cur.execute(query)
        result = cur.fetchone()
        if result[0] is None:
            return 0
        return result[0]

    @staticmethod
    def get_request():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM requests")
        data = cur.fetchone()
        return data

    @staticmethod
    def count_requests():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM requests")
        count = cur.fetchone()[0]
        return int(count)
    
    @staticmethod
    def get_all_data_request():
        data = {}
        cur= mysql.connection.cursor(dictionary=True)
        
        cur.execute("SELECT * FROM requests")
        data["requests"] = cur.fetchall()

        cur.execute("SELECT * FROM payments")
        data["payments"] = cur.fetchall()

        cur.execute("SELECT * FROM service_print")
        data["s_print"] = cur.fetchall()
        cur.close()
        return data
    
    #create a function to get values of request_id, order_status, location, description, mode_of_payment, and user_id
    @staticmethod
    def display_request():
        cur = mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT `request_id`, `user_id`, `order_status`, `location` FROM requests")
        requests = cur.fetchall()

        cur.execute("SELECT mode_of_payment FROM payments")
        payments = cur.fetchall()

        cur.execute("SELECT description FROM service_print")
        descriptions = cur.fetchall()
        data = {'requests': requests, 'payments': payments, 'descriptions': descriptions}
        return data