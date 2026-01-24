import random as rnd
import json



def words_select():
    with open("words.json",encoding="utf-8")as file:
        data = json.load(file)
        sansli =rnd.choice(data)
        return sansli

    
def print_kart(sansli):
    print(f"{'_'*22}\n"
    f"|{'Sefa TABU kartları'.center(20).title():<20}|\n"
    f"|{"buluncak kelime".center(20).upper():<20}|\n"
    f"|{sansli["BASEWORD"].center(20).title():<20}|\n"
    f"|{"":<20}|\n"
    f"|{"yasaklı kelimeler".center(20).upper():<20}|")
    for word in sansli["HELPERWORD"]:
        print(f"|{word.center(20).title():<20}|")
    print(f"|{"":<20}|")
    print(f"{'*'*22}")
    
# def tabu_baslat(callback=donus):
#     kart = words_select()
#     print_kart(kart)
#     while True:
#         secenek = input("tekrar oynayalımmı (hayır:( h) devam etmek için her hangi bir tuşa basın: ")
#         match secenek:
#             case "h":
#                 donus()
#             case _:
#                 kart = words_select()
#                 print_kart(kart)
def tabu_baslat(callback=None):
    kart = words_select()
    print_kart(kart)
    while True:
        secenek = input("tekrar oynayalımmı (hayır:( h) seçenek ekranına dönmek için h, devam için başka tuş): ")
        match secenek:
            case "h":
  # callback verilmişse onu çağır
                return callback()

            case _:
                kart = words_select()
                print_kart(kart)

