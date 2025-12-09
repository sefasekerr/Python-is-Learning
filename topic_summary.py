# def tekmiciftmi(x):
#     return print("tek" if x%2==1 else "cift")
# sayi = input("sayı girin: ")
# tekmiciftmi(sayi)

# def ort(*sayilar):
#     ortalama = sum(sayilar)/len(sayilar)
#     return print(ortalama)

# girisler = input("giriş yapınız: ")
# girisler = (int(i) for i in girisler.split() )
# ort(*girisler)

# def kackez(harf,*kelime):
#     adet = 0
#     for ch in kelime:
#         if harf == ch :
#             adet += 1
#     return print(f"{harf} harfi {adet} kere var.")

# cümle = input("cümleyi giriniz: ")
# harf = input("hangi harf: ")
# kackez(harf,*cümle)

# def toplama(*args):
#     return print(sum(args))

# def cikarma(sayi1,sayi2):
#     return print(f"sonuç: {sayi1 - sayi2 if sayi1 > sayi2 else sayi2- sayi1}")
        
# def carpma(sayi1,sayi2):
#     return print(f"sonuç: {sayi1*sayi2}")

# def bol(sayi1,sayi2):
#     return print(f"sanuç: {sayi1/sayi2 if sayi2 !=0 else "sıfıra bölünemez"}")

# import random as rnd

# rnds1 = rnd.randrange(2,50)

# def tahmin(sayi):
#     global rnds1
     
#     if sayi<rnds1:
#             print("arttır")
#             return 
#     elif sayi > rnds1:
        
#             return print("azalt")
    
# sayi = int(input("sayı girin: "))
# while sayi != rnds1:
#     tahmin(sayi)
#     sayi = int(input("sayı girin: "))
    
# print("tebriks")
person = {}

print(dir(person))
# print(help(person.clear))
print(help(person.values))
