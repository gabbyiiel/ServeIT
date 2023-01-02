from ServeIT import mysql

class Services:
    @staticmethod
    def add_print_request(userID,request_id, mode_of_payement, order_status, order_date, service_id, print_id, print_file, number_of_copies):
        cur = mysql.connection.cursor()
        # Check if the userID exists in the users table
        query = "SELECT * FROM users WHERE userID = %s"
        values = (userID,)
        cur.execute(query, values)
        user = cur.fetchone()
        if user:
            query = "SELECT * FROM s_print WHERE service_id = %s and file_ "

    @staticmethod
    def add_print_values(print_id, file, number_of_copies,specification,service_id):
        cur = mysql.connection.cursor()
        query = "INSERT INTO s_print (print_id, file, number_of_copies, specification, service_id) VALUES (%s, %s, %s, %s, %s)"
        values = (print_id, file, number_of_copies, specification, service_id)
        cur.execute(query, values)
        mysql.connection.commit()

    @staticmethod
    def get_service_type(service_id):
        cur = mysql.connection.cursor()
        # Select the service with the given service_id
        query = "SELECT * FROM services WHERE service_id = %s"
        values = (service_id,)
        cur.execute(query, values)
        # Fetch the service
        serviceID = cur.fetchone()
        # Return the service if it exists, or None if it does not exist
        return serviceID
        

    