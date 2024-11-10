from django.db import connection, DatabaseError
import mysql.connector
from mysql.connector import Error

class SQLHandler:
    def __init__(self):
        self.host_name = "sql12.freesqldatabase.com"
        self.user_name = "sql12735044"
        self.password = "CY1bvbWVQf"
        self.database = "sql12735044"
        self.connection = mysql.connector.connect( 
            host = self.host_name,
            user = self.user_name,
            passwd = self.password,
            db = self.database
        )
    
    def update_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except DatabaseError as e:
            print(e)
    def read_query(self, query):
        cursor = self.connection.cursor()
        results = []
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except:
            print("error")
        

