from datetime import datetime
class Register:
    def __init__(self,name,surname,skor):
        self.name=name
        self.surname = surname
        self.username = Register.username_control()
        self.password = Register.password_control()
        self.id = Register.get_next_id()
        self.created_date = datetime.now().strftime(f"%d/%m/%Y, %H:%M:%S")
        self.skor = skor
        Register.user_save(self)
        
    def get_next_id():
        max_num=[]
        import json
        with open("users.json",encoding="utf-8") as file:
            ids = json.load(file)
            for k in ids.keys():
                k = int(k)
                max_num.append(k)
            return max(max_num)+1
        
    def username_control():
        import re
        import json
        while True:
            username = input("kullanıcı adınızı giriniz (küçük-büyük harfe duyarlıdır rakam kullanılabilir): ")
            pattern_u = r"^\w{5,21}$"
            if re.match(pattern_u,username):
                with open("users.json",encoding="utf-8") as file:
                    usernames = json.load(file)
                    for i in usernames.values():
                        if i["username"]==username:
                            print("kullanıcı adı alınmış")
                            break
                    else:
                        return username
            else:
                print("hatalı kullanıcı adı girişi!")
                
    def password_control():
        import re
        while True:
            password=input("şifrenizi giriniz: ")
            pattern_p = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!_]).{8,}$"
            if re.match(pattern_p,password):
                return password
            else:
                print("daha güçlü şifre oluşturun!!")

    def user_save(self):
        import json
        with open("users.json",encoding="utf-8") as f:
            data = json.load(f)
        data[self.id]={
                    "name":self.name,
                    "surname":self.surname,
                    "username":self.username,
                    "password":self.password,
                    "skor":self.skor,
                    "createddate":self.created_date
                    
                }
        with open("users.json","w",encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=1)
           
    def as_tuple(self):
        return (self.id, {
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password,
            "skor": self.skor,
            "createddate": self.created_date
        })


            
