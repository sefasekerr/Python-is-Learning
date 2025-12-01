# fiyatlar = input("Lütfen fiyatlarini aralarinda bosluk olacak sekilde giriniz giriniz: ")
# fiyatlar_listesi = [int(x) for x in fiyatlar.split()]
# print(f"Toplam fiyat: {sum(fiyatlar_listesi)}")

# fiyatlar = "12 121312 23 1312 413 124234   34245"
# fiyatlar_listesi = [int(x) for x in fiyatlar.split()]
# print(fiyatlar_listesi)
# print(sum(fiyatlar_listesi))  # 293551


# i = 0
# notlar = []
# while i<3:
#     notlar.append(float(input(f"{i+1}. notu giriniz: ")))   
#     i += 1
    
# print(F"ORTLAMANIZ: {sum(notlar)/len(notlar)}")    

# sifre = input("Lutfen guclu bir sifre giriniz: ")
# guclumu = sifre.isalnum() and len(sifre) >= 8 
# yazi = "şifreniz güçlüdür." if guclumu else "şifreniz güçlü değildir."
# print(yazi)

# sayi_sitesi = [1, 3, 5, 7, 9, 12, 19, 21]
# aranan = int(input("Lutfen aradiginiz sayiyi giriniz: "))
# var_mi = aranan in sayi_sitesi
# yazi = f"{aranan} sayisi sitede bulunmaktadır." if var_mi else f"{aranan} sayisi sitede bulunmamaktadir."
# print(yazi)

# web = input("Lutfen bir web adresi giriniz: ")
# guvenli_mi = web.startswith("https")
# yazi = "website is secure." if guvenli_mi else "website is not secure."
# print(yazi)

# fiyatlar = []
# for i in range(3):
#     fiyatlar.append(float(input(f"Lutfen {i+1}. fiyati giriniz: ")))
# toplam = sum(fiyatlar)
    
# yazi = f"toplam fiyat 500den fazla {toplam *0.90} %10 indirim kazandınız." if toplam > 500 else f"toplam fiyat: {toplam}"

# print(yazi)