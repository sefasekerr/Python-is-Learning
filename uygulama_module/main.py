from methods import *

def menu():
    print(f"mağazaya hoşgeldiniz\n"
        f"1-yeni ürün ekleyebilirsiniz\n"
         
        f"2-ürün güncellemesi\n"
         
        f"3-ürünleri listeleyin")
    islem = input("ne yapacaksınız: ")
    #

    if islem =="1":
        urunadi = input("ürünün adını giriniz: ")
        fiyat = int(input("ürünün fiyatı nedir: "))
        urun_ekle(urunadi,fiyat)
        return menu()
        
    elif islem =="2":
        id = int(input("id bilgisi nedir: "))
        urunadi = input("ürünün adını giriniz: ")    
        fiyat = int(input("ürünün fiyatı nedir: "))
        urun_guncelle(urunadi,fiyat,id)
        return menu()
        
    elif islem=="3":
        sonuc = urunleri_goruntule()
        for i in sonuc:
            print(i["urunadi"])
        return menu()
menu()  