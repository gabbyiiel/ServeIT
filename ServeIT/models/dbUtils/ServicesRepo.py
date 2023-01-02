from ServeIT import mysql

class Services:
    @staticmethod
    def add_request():
        cur = mysql.connection.cursor()