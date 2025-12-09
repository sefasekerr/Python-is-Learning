
# bittimi = "a"
# a = True
# toplam= 0
# while a:
#     if a:
#         fiyat = float(input("Fiyat giriniz: "))
#         miktar = float(input("Miktar giriniz: "))
#         bittimi = input("bitmediyse boş geçiniz bittiyse bitti yazın: ")
#         a = False if bittimi =="bitti" else True
#         toplam += fiyat*miktar
#     else:
#         break
# print(toplam)


sayi = 9

# sansliTahmin = int(input("sayı tahmin edin: "))
tahminler = []
dogrumu = True
while dogrumu:
    sansliTahmin = int(input("sayı tahmin edin: "))
    if sansliTahmin !=sayi:
        print("yanlış tahminn")
        tahminler.append(sansliTahmin)
    else:
        print(f"tebrikss buldunuz {sansliTahmin} tahminleriniz:{tahminler}")     
        dogrumu=False