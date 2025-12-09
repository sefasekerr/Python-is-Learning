hesaplar = [
    {
        "ad":"Sefa ŞEKER",
        "hesap numarsı":"28022025",
        "username": "sefaseker60",
        "password": "654321",
        "bakiye":50000,
        "ekhesap":75000
    },
    {
        "ad":"hiranur ŞEKER",
        "hesap numarsı":"06012013",
        "username": "bensalagım",
        "password": "123456",
        "bakiye":5000,
        "ekhesap":700        
    }
]
def bakiyesorgulama(hesap):
    print(f" güncel bakiye {hesap["bakiye"]}\n ek hesap bakiyeniz {hesap["ekhesap"]} ")


def paracekme(hesap):
    miktar = int(input("çekeceğiniz tutarı giriniz: "))
    if miktar>= (hesap["ekhesap"]+hesap["bakiye"]):
        print("yetersiz bakiye")
    elif miktar>=hesap["bakiye"]:
        miktar -= hesap["bakiye"]
        hesap["ekhesap"]-= miktar
        hesap["bakiye"] = 0
    else:
        hesap["bakiye"]-=miktar
        return menu(hesap)  

def parayatirma(hesap):
    miktar = int(input("yatırmak istediğiniz tutar: "))
    hesap["bakiye"] += miktar




def menu(hesap):
    print(f"""
merhaba {hesap["ad"]}
güncel bakiye {hesap["bakiye"]}
ek hesap limitiniz {hesap["ekhesap"]}             
          """)
    secenek = input(f"""
1 - bakiye sorgula
2 - para çekme 
3 - para yatırma 
Yapmak istediğiniz işlemi seçiniz: """)
    
    
    if secenek == "1":
        bakiyesorgulama(hesap)
    elif secenek == "2":
        paracekme(hesap)
    elif secenek == "3":
        parayatirma(hesap)
    else :
        print("hatalı giriş")
    menu(hesap) 


user_name = input("kullanıcı adını girin: ")
password = input("şifreyi girin: ")

for hesap in hesaplar:
    if  hesap["username"] == user_name and  hesap["password"] == password :
        menu(hesap)
        break
else:
    print("hatalı giriş.")    
    
    

 
    
    



    
    


