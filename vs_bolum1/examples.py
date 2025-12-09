# - Eğer kullanıcı adı "sefa" ve şifre "1234" ise → “Giriş başarılı”.
# - Eğer kullanıcı adı doğru ama şifre yanlışsa → “Şifre hatalı”.
# - Eğer kullanıcı adı yanlışsa → “Kullanıcı bulunamadı”.
# - Ekstra: Eğer 3 kez yanlış girerse → “Hesap kilitlendi”.

# userName = "sefa"
# userPassword = 1234
# for i in range(1,4):
#     loginUserName = input("kullanıcı adını giriniz: ")
#     login_user_password = int(input("şifrenizi girin: "))
#     if ( loginUserName == userName and login_user_password == userPassword):
#         print("giriş yapılıyor.")
#         break
#     else:
#         print(f"{"hesap kitlendi" if (i==3) else ("kalan deneme hakkı: " f"{3-i}")}")

"""
    - Kullanıcıdan yaş, gelir, borç durumu bilgisi al.
- Eğer yaş < 18 → “Başvuru reddedildi (yaş yetersiz)”.
- Eğer gelir < 5000 ve borcu varsa → “Başvuru reddedildi (gelir ve borç durumu uygun değil)”.
- Eğer gelir >= 5000 ve borcu yoksa → “Başvuru onaylandı”.
- Eğer gelir >= 5000 ama borcu varsa → “Ek inceleme gerekli”.

"""


# user_age = int(input("yaşınız nedir: "))
# user_income = float(input("aylık geliriniz ne kadar: "))
# user_debt_info = True if (input("borcunuz varmı(var/yok şeklinde): ".strip()) == "var")else False
# if (user_age < 18):
#     print("yaş yetersiz.")
# elif ( user_income<5000):
#     print("gelir yetersiz")
# elif ( user_debt_info):
#     print("borç var")
# elif ( user_income>=5000 and user_debt_info):
#     print("ek inceleme şart.")
# else:
#     print("tebriks:)")

"""
- Eğer can <= 0 → “Karakter öldü”.
- Eğer can > 0 ama enerji <= 0 → “Karakter yorgun, dinlenmeli”.
- Eğer can > 50 ve enerji > 50 → “Karakter güçlü durumda”.
- Eğer can < 50 ve enerji > 50 → “Karakter yaralı ama enerjik”.
- Eğer can > 50 ve enerji < 50 → “Karakter sağlam ama yorgun”.
"""

# health_point = int(input("can kaç: "))
# energy= int(input("enerji seviyeniz kaç: "))
# if (health_point==0):
#     print("karakter öldü")
# else:
#     if((101>health_point>50)and (101>energy>50)):
#         print("karakter sağlam")
#     elif((101>health_point>50)and (0<energy<=50)):
#         print("karakter yorgun")
#     elif((0<health_point<=50)and (101>energy>50)):
#         print("karakter yaralı ama çalışır")
#     elif ((101>health_point>0)and (energy==0)):
#         print("dinlenmek lazım")
#     else:
#         print("hatalı giriş")

"""
- Ekonomi sınıfı için: bagaj hakkı 20 kg.
- Business sınıfı için: bagaj hakkı 30 kg.
- Eğer bagaj hakkı aşılırsa → “Ekstra ücret ödeyin”.
- Eğer aşılmazsa → “Check-in başarılı”.
"""

# ticket_classes = {
#     "ekonomi":{
#         "baggage_limit": 20,
#     },
#     "business":{
#         "baggage_limit": 30,
#     }
# }
# user_ticket = input("hangi tür bilet: ")
# if (user_ticket in ticket_classes):
#     if ( user_ticket=="ekonomi"):
#         print("bagaj limitiniz 20 kg")
#         baggage = int(input("kaç kg: "))
#         print(f"aşılmadı" if ( baggage<=ticket_classes["ekonomi"]["baggage_limit"])else"aşıldı")
#     else:
#         print("bagaj limitiniz 30 kg")
#         baggage = int(input("kaç kg: "))
#         print(f"aşılmadı" if ( baggage<=ticket_classes["business"]["baggage_limit"])else"aşıldı")
# else:
#     print("hatalı griş")