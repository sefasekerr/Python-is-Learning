# def isim(isim):
#     return print(isim)

# isim("sefa")

# def alan_cevre_hesaplaması(uzunkenar,kisakenar):
#     alan = uzunkenar*kisakenar
#     cevre = 2*(uzunkenar+kisakenar)
#     return print(f"""
# v2.5erilern bilgiler ışığında çevresi: {alan}
# verilern bilgiler ışığında çevresi: {cevre}""")

# uzunkenar = float(input("uzunkenarı girinz: "))
# kisakenar = float(input("kisakenarı girinz: "))

# alan_cevre_hesaplaması(uzunkenar,kisakenar)

# def bolensayisi(sayi):
#     sayiListesi = list(a  for a in range(1,sayi) if sayi%a==0)
#     return print(sayiListesi)


# sayi = int(input("sayiyi girin:" ))

# bolensayisi(sayi)
# print("sefa")

# def yaziTura():
#     import random as rnd
#     x = rnd.random()

#     yT = "yazı" if (0.5< x) else "tura"
#     return print(yT)


# yaziTura()
# adet=0
# finish_num = int(input("sayıyı giriniz: "))
# start_num = int(input("başlangıç sayısını girin: "))
# sonuc = []
# def asalmi(start_num,finish_num):
#     for i in range(start_num,finish_num+1):
#         adet=[]
#         adet = sum(1 for b in range(2,i+1) if  i % b==0)
#         if adet == 1:
#             sonuc.append(f"asaldır: {i}")

#     return sonuc

# print(asalmi(start_num,finish_num))

# a=2
# while a<=i:
#     if i%a==0:
#         adet+=1
#     a+=1
# if adet==1:
#     sonuc.append(f"asaldır: {i}")
# sonuc.append(f"{(f"asaldır {i}")  if adet ==1 else 0}")


print("Sefa Bankasına Hoşgeldiniz:)")

balance = 18000


def parayatirma(yatacakTtr=int):
    global balance
    balance += yatacakTtr
    sonuc = f"yeni bakiye: {balance}"
    return sonuc


def paracekme(cekecekTtr=int):
    global balance
    balance = balance - cekecekTtr
    sonuc = f"yeni bakiye: {balance}"
    return sonuc


def sorgulama():
    sonuc = balance
    return sonuc


kayitli = [
    {
        "user_name": "Sefa Şeker",
        "password": "Pekmez2001",
        "bakiye": 50000
    },
    {
        "user_name": "Şeker Sefa",
        "password": "2004Ceviz",
        "bakiye": 35000
    }
]


def account(isim, sifre):

    # isim = kayitli.get("user_name".strip)
    # sifre = kayitli.get("password"
    if isim == kayitli.get["user_name"] and sifre == kayitli.get["password"]:
        islem = int(input(
            "hangi işlemi yapacaksınız\n 1=para yatırma \n 2=para çekme \n 3=bakiye sorgulama \n :"))

        if islem == 1:
            miktar = int(input("ne kadar yatıracaksınız: "))
            sonuc = parayatirma(miktar)
            return sonuc

        elif islem == 2:
            miktar = int(input("ne kadar çekeceksiniz: "))
            sonuc = paracekme(miktar)
            return sonuc

        elif islem == 3:
            sonuc = sorgulama()
            return sonuc

        else:
            sonuc = print("hatalı giriş!")
            return sonuc

    else:
        sonuc = "hatalı giriş"
        return sonuc


isim = input("isminiz nedir:")
sifre = input("şifreniz nedir: ")
print(account(isim, sifre))
