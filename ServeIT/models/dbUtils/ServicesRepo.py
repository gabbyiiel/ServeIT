from ServeIT import mysql



class Services:
    
    @staticmethod
    def add_request(order_status, order_date, mode_of_payment):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'SELECT * from users where userID = "{userID}"')
            result = cur.fetchone()
            if result is not None:
                userID = result[0]
            else:
                return {
                    'code': -1,
                    'message': 'User not found'
                }
            cur.execute(f''' INSERT INTO `requests`
                        (`request_id`, `userID`, `service_id`, `order_status`, `order_date`, `mode_of_payement`)
                        VALUES ('', '{userID}', '', '{order_status}', '{order_date}', '{mode_of_payment}')''')
            mysql.connection.commit()
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
    def add_printing(fileURL, num_copies, specification):
        try:
            cur = mysql.connection.cursor()
            cur.execute(f''' INSERT INTO `s_print`
                        (`print_id`, `service_code`,`file`, `number_of_copies`, `specification` ) 
                        VALUES ('','', '{fileURL}', '{num_copies}', '{specification}')''')
            mysql.connection.commit()
            print("success")
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
    def add_service(service_name):
        try:
            cur = mysql.connection.cursor()
            # Retrieve the maximum value of the service_code column
            cur.execute("SELECT MAX(service_code) FROM services")
            result = cur.fetchone()
            max_service_code = result[0]

            # Extract the number part from the maximum service code
            # and increment it by 1
            if max_service_code:
                number_part = int(max_service_code.split("SCSD")[1]) + 1
            else:
                # If the services table is empty, start the service code from 1
                number_part = 1

            # Generate the new service code
            service_code = "SCSD" + str(number_part).zfill(4)

            # Generate the service_name
            service_name = f"SF{service_name}"

            cur.execute(f''' INSERT INTO `services`
                        (`service_code`, `service_name`)
                        VALUES ('{service_code}', '{service_name}')''')
            mysql.connection.commit()
            print("SERVICES ADDED")
            return {
                'code': 1,
                'message': 'SERVICES Added' }
        except Exception as e:
                print(e)
                return {
                    'code': -1,
                    'message': f'{e}'
                }