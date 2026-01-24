import hashlib
import pyodbc
from database import Database
class Login :
        
    def login_control():
        username = input("kullanıcı adınızı giriniz: ")
        password=input("şifrenizi giriniz")
        password  = hashlib.sha3_256(password.encode()).hexdigest()
        databe = Database.get_connection()
        cursor = databe.cursor()
        sql = "select * from players where username=? and password=?"
        values = (username,password)
        cursor.execute(sql,values)
        i = cursor.fetchone()
        baslik = [col[0] for col in cursor.description]
        if i is not None:
            salak = dict(zip(baslik,i))
            print(salak)
            
        else :
            print("kayıt bulunamadı kayıt olmak istermisiniz?")
        
user = Login.login_control()