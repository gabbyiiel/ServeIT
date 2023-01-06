from ServeIT import mysql



class Services:
    
    @staticmethod
    def add_request(userID, order_status, mode_of_payment):       
        service_code = Services.get_service_code()
        try:
            cur = mysql.connection.cursor()
            # Retrieve the maximum value of the request_id column
            cur.execute("SELECT MAX(request_id) FROM request_id")
            result = cur.fetchone()
            max_request_code = result[0]
            # Extract the number part from the maximum request code
            # and increment it by 1
            if max_request_code:
                number_part = int(max_request_code.split("SDRQID")[1]) + 1
            else:
                # If the request table is empty, start the request code from 1
                number_part = 1
            # Generate the new request id code
            request_id = "SDRQID" + str(number_part).zfill(4)

            cur.execute(f''' INSERT INTO `requests`
                        (`request_id`, `user_id`, `service_code`, `order_status`, `order_date`, `mode_of_payement`)
                        VALUES ('{request_id}', '{userID}', '{service_code}', '{order_status}', NOW(), '{mode_of_payment}')''')
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

    @staticmethod
    def add_printing(fileURL, num_copies, specification):
        service_code = Services.get_service_code_name("SFPR")
        try:
            cur = mysql.connection.cursor()
            cur.execute(f''' INSERT INTO `s_print`
                        (`print_id`, `service_code`,`file`, `number_of_copies`, `specification` ) 
                        VALUES ('','{service_code}', '{fileURL}', '{num_copies}', '{specification}')''')
            mysql.connection.commit()
            print("Print Service Added")
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
            service_code = "SDSC" + str(number_part).zfill(4)

            # Generate the service_name
            service_name = f"SF{service_name}"

            cur.execute(f''' INSERT INTO `services`
                        (`service_code`, `service_name`)
                        VALUES ('{service_code}', '{service_name}')''')
            mysql.connection.commit()
            return {
                'code': 1,
                'message': 'SERVICES Added' }
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