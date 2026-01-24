import json
from register import Register
class Login(Register):

    def login_control():
        with open("users.json",encoding="utf-8") as file:
            data = json.load(file)
        for hak in range(3,0,-1):
            username = input("kullanıcı adınız giriniz.")
            password = input("şifrenizi giriniz.")
            for user_id,user_info in data.items():
                if user_info["username"] == username and user_info["password"]==password:
                    print("giriş başarılı yönlendiriliyorsunuz...")
                    return (user_id,user_info)
            else:print(f"giriş başarısız tekrar deneyin(kalan hak {hak-1})")
        else:print("hakkınız bitti daha sonra tekrar deneyin!")
        return None
    
    def info_update(user_id,user_info):
        secenek = input(
        f"isim(1)/soyisim(2)/kullanıcı adı(3) değiştirilebilir "
        f"(hesap oluşturulma tarihi: {user_info.get("createddate", "bilgi yok")}): "
    )
        match secenek:
            case "1":
                name=input(f"isminizi giriniz(mevcut isim {user_info['name']}): ")
                user_info["name"]= name

            case "2":
                surname=input(f"isminizi giriniz(mevcut isim {user_info['name']}): ")
                user_info["surname"]= surname

            case "3":
                username=Register.username_control()
                user_info["username"]= username
            case "4":
                password = Register.password_control()
                user_info["password"]= password
            case _ :
                print("hatalı tuşlama (sayı giriniz)")
                return

        with open("users.json",encoding="utf-8") as f:
            data = json.load(f)
        data[str(user_id)] = user_info

        with open("users.json","w",encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=1)
    
