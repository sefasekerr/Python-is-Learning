import sys
import pyodbc as dbs

database = dbs.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=192.168.1.6;"
    "Database=ETRADE4;"
    "UID=sa;"
    "PWD=Sefa1234;"
)
cursor = database.cursor()
cursor.execute("select * from USERS")

print(len(cursor.fetchall()))
# for row in cursor.fetchall():
#     print(row)

print(database)

print(sys.getsizeof(database))
# print(cursor.tables().fetchall())
cursor.columns(table="USERS")
for row in cursor.fetchall():
    new_row=[]
    for i in row:
        if i ==   None:
            continue
        else:
            new_row.append(i)
    
    print(new_row)