import pyodbc as dbs
import hashlib

database = dbs.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=192.168.1.6;"
    "Database=satranc;"
    "UID=sa;"
    "PWD=Sefa1234;",
    autocommit=True
)
cursor = database.cursor()

sql = "INSERT INTO players ( username) VALUES (?)"

data = ("sefasekerr")

cursor.execute(sql,data)
database.commit()