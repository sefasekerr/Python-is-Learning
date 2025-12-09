# a, b, c = 4,8,(12,2)

# sayi1 = int(input("sayı giriniz: "))
# sayi2 = int(input("sayı2 giriniz: "))
# result1= (sayi1*sayi2) - ( a+ b+ sum(c))
# result2= sum(c)//b
# result3 = (a+b+sum(c))%7
# result4 = b**a
# x,*y,z=(2,4,6,8,13)
# result5 = (
#     z**2
# )
# k,l,*m = (2,4,6,8,13)
# result6 = sum(m)


# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)

# sayi1= int(input("sayı girin: "))
# sayi2= int(input("sayı girin: "))

# buyukolan= "sayi2 büyük " if (sayi1<sayi2) else "sayi1 büyük"
# print(buyukolan)

# tekmi= "tek " if (sayi1 % 2 ==1) else "çift"
 
# for i in range(3):
#     notlar = float(input(f"{i+1} notunuz ne: "))
#     print(f"sonuç: {"başarılı"if notlar>50 else "başarısız"}")

# yas = int(input("yaşınız kaç: "))
# izin = input("izin varmı(var ya da yok yazın): ".strip())
# izinVarmi = True if (izin == "var") else False

# sonuc = (yas >= 18 or izinVarmi)
# print(sonuc)

# dersNotu= float(input("notunuz kaç: "))
# print(f"sonucunuz: {"geçti" if (100>dersNotu>50) else "kaldı"}")

# notOrt = float(input("ortalamanız kaç: "))
# zayifVarmi= input("varsa var yoksa yok yazınız: ")
# zayifSonuc = True if (zayifVarmi=="yok")else False
# sonuc = notOrt>=70 and zayifSonuc
# print(sonuc)

# mezuniyet=input("ne mezunusunuz: ".strip())
# enAzSart = ["önlisans","lisans"]
# sonuc = "tebbrşkler işe alındınız" if ( mezuniyet in enAzSart ) else "biz sizi ararız"
# print(sonuc)

# userName = "Sefa9"
# userMailAdress= "sefaseker92@gmail.com"
# password= "Rewind280225"

# loginInfo = input("kullanııcı adı ya da mail adresini girin: ")
# loginPassword = input("şifreyi girin: ")

# info = True if (userMailAdress==loginInfo or userName==loginInfo )else False
# loginPass = True if (password==loginPassword)else False
# print(f"{"giriş yapıldı" if (info and loginPass)else "hatalı giriş"}")

# yakitTipi = input("yakıt türü nedir: ")
# miktar = float(input("ne kadar alacaksınız: "))
# benzin , dizel , lpg = 39.39,41.71,20.28
# if (yakitTipi=="benzin"):
#     print(f"ödenecek tutar: {miktar*benzin}")
# elif (yakitTipi=="dizel"):
#     print(f"ödenecek tutar: {miktar*dizel}")
# elif ( yakitTipi=="lpg"):
#     print(f"ödenecek tutar: {(miktar*lpg):.2f}")
# else:
#     print("yanlış hataa")    
    
# yazilinotlari=[]
# for i in range(2):
#     yazilinotlari=float(input("notlarınız:"))
    
# sozluNotu= float(input("sözlü notu: "))
# sonuc = (sum(yazilinotlari) +sozluNotu) /3
# if ( 0<sonuc<25):
#     print("sonuc : 0")
# elif( 25<sonuc<45):
#     print("sonuc : 1")
# elif(45<sonuc<55):
#     print("sonuc : 2")
# elif(55<sonuc<70):
#     print("sonuc : 3")
# elif(70<sonuc<85):
#     print("sonuc : 4")
# elif(85<sonuc<101):
#     print("sonuc : 5")
# else:
#     print( "hatalı giriş")    


























