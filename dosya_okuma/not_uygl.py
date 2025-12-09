def not_gir():
    ad = input("isim girişi yapınız: ")
    soyad = input("soyisim girişi yapınız: ")
    not1 = input("not 1 :")
    not2= input("not 2 :")
    not3 = input("not 3 :")
    with open("notgirisi.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad} : {not1},{not2},{not3}\n")
        
        
def not_ort(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ad = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    return f"{ad} isimli öğrencinin ort: {(not1+not2+not3)/3}\n"        
        
        
        
def notlar():
    with open("notgirisi.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_ort(satir))




def not_kaydet():
    with open("notgirisi.txt","r",encoding="utf-8") as file2:
        liste = []
        for satir in file2:
            liste.append(not_ort(satir))
            
        with open("sivansonuclari.txt","w",encoding="utf-8") as file:
            file.writelines(liste)
            
        
    with open("sinavsonuclar.txt","w",encoding="utf-8") as file:
            file.write(f"")
        
        
while True:
    islem = input(f"1-not girişi\n2-not ortalaması\n3-notları kaydet\n4-çıkış\nseçim yapın:")
    if islem == "1":
        not_gir()        
        
    elif islem=="2":
        notlar()
        
    elif islem == "3":
        not_kaydet()
        
    else:
        break
