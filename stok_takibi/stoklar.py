from islemler import *

while True:
    print(f"Sefa Market Hoşgeldiniz\n"
          f"1-ürünleri sorgulama\n"
          f"2-ürünleri hesaplayın\n"
          f"3-çıkış\n"
          f"4-ürün ekle\n")
    islem = input("seçim yapınız: ")
    
    
    
    if islem == "1":
        urunnick = input("hangi ürünü sorgulayacaksınız: ")        
        print(urun_sorgula(urunnick))
        
    elif islem == "2":
        urunnick = input("hangi ürünü sorgulayacaksınız: ")        
        miktar = int(input("ne kadar aldınız: "))
        
        print(fiyat_hesaplama(urunnick,miktar))
    elif islem=="4":
        product_name = input("ürün ismi giriniz: ")
        price = float(input("fiyat girin: "))
        stock = int(input("stok giriniz: "))
        urun_ekle(product_name,price,stock)

        
        
    
    