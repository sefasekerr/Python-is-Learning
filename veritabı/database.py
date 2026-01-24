import pyodbc

class Database:
    _connection = None
    @staticmethod
    def get_connection():
        if Database._connection is None :
            Database._connection = pyodbc.connect(
              "Driver={ODBC Driver 17 for SQL Server};"
                "Server=192.168.1.6;"
                "Database=sokmarket;"
                "UID=sa;"
                "PWD=Sefa1234;",
                autocommit=True  
            )
        return Database._connection