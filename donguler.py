# -*- coding: utf-8 -*-

# sayiler = [3,5,7,2,12,32,45]
# toplam = 0
# for sayi in sayiler:
#     print(sayi)

# for (x ) in  sayiler:
#    print(f"tam katı olanlar: {x } "   if x%3 ==0 else f"tam katı olmayalar:  {x}")
   
# for a in sayiler:
#     toplam += a
   
# print(toplam)
# adet = 0
# ürünler = ["samsung s24","samsung s22","iphone 15","iphone 14"]
# for ürün in ürünler: 
#     if "samsung" in ürün:
#         adet +=1
#     else:
#         print(ürün)
# print(adet)

urunler = [
    {"urun_adi": "hp victus", "fiyat":32999},
    {"urun_adi": "lenovo thinkpad", "fiyat":25499},
    {"urun_adi": "apple macbook", "fiyat":49999},
    {"urun_adi": "huawei matebook", "fiyat":26999},
    {"urun_adi": "casper nirvana", "fiyat":20000},
]
# toplam = 0
# for i in urunler:
#     toplam += i["fiyat"] 
#     print(f"{i["urun_adi"]} markalı ürünün fiyatı {i["fiyat"]}")
# for i in urunler:
#     if 25000<i["fiyat"]<=40000:
#         print(f"{i["urun_adi"]} markalı ürünün fiyatı {i["fiyat"]}")
    
# print(toplam)

# user_keys_info = input("hangi ürünü öğrenmek istiyorsunuz: ".strip())
# for a in urunler:
    
#     if user_keys_info in a["urun_adi"] :
#         print(f"{a["urun_adi"]} markalı ürünün fiyatı {a["fiyat"]}")
        
    
# start_num = int(input("başlangıç değerini giriniz: "))
# end_num = int(input("bitiş değerşnş giriniz: "))

# while start_num<=end_num:
#     if start_num % 2 == 0:
#         print(start_num)
#     start_num += 1
    
# a , b = 1 , 100
# while b>=a:
#     print(b)
#     b-=1

# numbers = []
# for i in range(1,6):
#     numbers.append(int(input(f"{i}. sayıyı girin: ")))
    
# print(sorted(numbers))

# user_name = ""
# while not user_name:
#     user_name = input("kullanıcı adınızı giriniz: ")
    
# print(user_name)
  
# students_info = {}  
# liste = []  
# bilgiler = [
#     'ogrencino ',
#     'ogrenciadi',
#     'ogrencisoyad'
# ]
# devammi=True
# while devammi:  
#     for bilgi in bilgiler:
#         students_info[bilgi] = input(f"{bilgi} giriniz: ")
#     a = input("yeni öğrenci eklicekmisiniz: ".strip())
#     liste.append(students_info)
#     devammi= True if a =="evet" else False
    
# print(students_info)
    
# print(liste)
# range()

# urunler = []
# fiyatlar = []
# bittimi = False
# toplam = 0

# while not bittimi:
#     urunler.append(input("ne aldınız: "))
#     fiyatlar.append(float(input("fiyatı ne kadar: ")))
#     bittimi = True if (input("bu kadarmı: ")=="evet")else False
    
# sonuc = list(zip(urunler,fiyatlar))
# for a,b in sonuc:
#     print(f"{a} isimli ürünün fiyatı {b}")
    
# print(f"toplam ücret: {sum(fiyatlar)}")
"""
- Kullanıcıdan öğrenci adı ve notunu al.
- Notu listeye ekle.
- 3 öğrenci girildikten sonra ortalamayı hesapla.
- Ortalama 50’den büyükse “Geçti”, değilse “Kaldı” yazdır.
"""
ogrenci_no = []
ogrenci_adi = []
ogrenci_notu = []
ort = []
toplam=0

i = a = 0

while i in range(3):
    ogrenci_no.append(input("ogrencinin numarası nedir: "))
    ogrenci_adi.append(input("öğrenci ad: "))
    while a in range(3):
        ogrenci_notu.append(int(input(f"{ogrenci_adi[i]}isimli öğrencinin {a+1}. notu: ")))
        toplam = int(sum(ogrenci_notu))
        a+=1
    ort.append((toplam/3)) 
    a = 0
    i+=1
     

ogrenciler = list(zip(ogrenci_no,ogrenci_adi,ort))
#

hangi_ogrenci = input("öğrencinin ismi: ")
y=0

if hangi_ogrenci in ogrenci_adi:


    print(hangi_ogrenci)
    
            


"""

notlar={
    sefa:{
        1.not:
        2.not:
        3.not:
    }
    zeynep:{
        1.not:
        2.not:
        3.not:
    }
    ahmet:{
        1.not:
        2.not:
        3.not:
    }
}
    
"""
# print(ogrenciler.setdefault("ogrenci_adi","bu öğrenci yoktur"))






