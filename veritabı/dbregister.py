import pyodbc
import hashlib
import re
import sys
from database import Database

class Register:
    
    def __init__(self,name,surname):
        self.__name = name
        self.__surname = surname
        self.__username = self.username_control()
        self.__password = self.password_control()
        self.__email = self.email_control()
    @property
    def name(self):return self.__name    
    @property
    def surname(self): return self.__surname    
    @property
    def username(self):return self.__username    
    @property
    def password(self):return self.__password    
    @property
    def email(self):return self.__email    
            
    def username_control(self):
        username=input("kullanıcı adınızı giriniz: ")
        pattern_u= r"^[a-zA-Z0-9]{8,16}$"
        
        if re.match(pattern_u,username) :
            return username
        else:
            print("Kullanıcı adı 8-16 karakter olmalı ve sadece harf/rakam içermeli.")
            return self.username_control()
        
        
    def password_control(self):
        password=input("şifrenizinizi giriniz: ")
        pattern_p = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern_p,password):
            return hashlib.sha3_256(password.encode()).hexdigest()
        else :
            print("uygun olmayan format")
            return self.password_control()
    def email_control(self):
        email = input("mail adresinizi giriniz: ")   
        pattern_m = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern_m,email):
            return email
        else:
            print("hatalı e-mail türü!")
            return self.email_control()
        
        
    def db_save(self):
        try:
            database = Database.get_connection()
            cursor = database.cursor()
            sql = "INSERT INTO players (name_, surname, username, password, email)OUTPUT INSERTED.player_id                                           VALUES (?, ?, ?, ?, ?)"
        
            values = (self.name,self.surname,self.username,self.password,self.email)
                
            cursor.execute(sql,values)
            user = cursor.fetchone()  
            baslik = [i[0]for i in cursor.description ]
            users = dict(zip(baslik,user))
                    
            return users
        except pyodbc.IntegrityError:
            print("kullanıcı adı alınmış!")
            return None

    
    def run_register():
        name =input("isminizi giriniz: ")
        surname = input("soy isminizi giriniz: ")
        while True:
            user= Register(name,surname)
            result = user.db_save()
            if result is not None:
                print(f"başarıyla kayıt olundu: ID={result['player_id']}")
                return result
            else:
                print("kullanıcı adı alınmış tekrar giriniz: ")
            
Register.run_register()    
        
