
import pyodbc
import hashlib
from database import Database


databases = Database.get_connection()
cursor = databases.cursor()
sql = "INSERT INTO players (name_, surname, username, password, email) VALUES (?, ?, ?, ?, ?)"

sorgu="select * from players where username=? and password=?;"

def login():
    name = input("isiminizi giriniz: ")
    surname = input("soy isiminizi giriniz: ")
    username = input("kullanıcı adınızı giriniz: ")
    password= input("şifre oluşturun: ")
    email = input("mail adresinizi giriniz: ")
    hashed_password = hashlib.sha3_256(password.encode()).hexdigest()

    cursor.execute(sql,(name,surname,username,hashed_password,email))
    try:
        cursor.execute("select * from players;")
        for row in cursor.fetchall():
            print(row[1],row[3])
    except pyodbc.IntegrityError as err:
        print("hata")

# cursor.columns(table="players")
def register():
    username = input("kullanıcı adınızı giriniz: ")
    password = input("şifrenizi giriniz: ")
    
    hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
    
    cursor.execute(sorgu,(username,hashed_password))
    i= cursor.fetchone()

        
  
cursor.execute("select * from players where player_id=1") 
i=[col[0] for col in cursor.description]
aaa= dict(zip(i,cursor.fetchone()))
print(aaa)