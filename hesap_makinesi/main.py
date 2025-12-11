import islemler

while True:

    try:
        sayi1 = int(input("1. sayıyı giriniz: "))
        sayi2 = int(input("2. sayıyı giriniz: "))
        islem = input("hangi islemi yapacaksınız (/,*,-,+): ")


        if islem == "/":
            sonuc =islemler.Hesap_Makinesi.bolme(sayi1,sayi2)
            print(sonuc)
        elif islem == "*":
            sonuc =islemler.Hesap_Makinesi.carpma(sayi1,sayi2)
            print(sonuc)
        elif islem == "-":
            sonuc =islemler.Hesap_Makinesi.cikarma(sayi1,sayi2)
            print(sonuc)
        elif islem == "+":
            sonuc = islemler.Hesap_Makinesi.toplam(sayi1,sayi2)
            print(sonuc)
        else:
            print("hatalı seçim")
    except Exception as ex:
        with open("hatalar.txt","a",encoding="utf-8") as f:
            f.write(f"{ex}\n")
            
        print(ex) 
    else:
        break
    
    
    
    
    
    # with open("hatalar.txt","r",encoding="utf-8") as f:
    #     satirlar = f.readlines()
    # with open("hatalar.txt","r+",encoding="utf-8")as file:           
    #     for satır in satirlar:
        
    #         file.write(f"{satır}\n")
    #     file.write(ex)
      