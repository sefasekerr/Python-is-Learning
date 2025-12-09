def not_gir():
    ad = input("adınızı girin: ")
    soyad = input("soyadınızı girin: ")
    not1 = input("1. notu girin: ")
    not2 = input("2. notu girin: ")
    not3 = input("3. notu girin: ")
    
    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad} isimli öğrencinin ortalaması : {not1}, {not2}, {not3} \n")  
    pass

def notları_oku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for ogrenciler in file:
            not_hesapla(ogrenciler)
    pass

def not_ort():
    
    with open("notlar.txt","r",encoding="utf-8") as file:
        toplam= 0    
        for ogrerci in file:
            nots = ogrerci.split(":")
            for notlar in nots[1].split(","):
                toplam = toplam + int(notlar)
            print(toplam/3)
            toplam= 0   
 
def not_kaydet():
    pass

def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    isim= liste[0]
    notlar = liste[1].split(",")
    print(f"{isim}: {(int(notlar[2])+int(notlar[1])+int(notlar[0])) / 3}")






while True:
    islem = input("1-not girişi\n2-ortalama göster\n3-notları kayıt et\n4-cıkış\nseçim:")
    if islem == "1":
        not_gir()
    elif islem== "2":
        notları_oku()
        
    elif islem== "3":
        not_kaydet()
        
    else:
        break

        
        
        
        
        
    