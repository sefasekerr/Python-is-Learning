
# class banka_hesap:    
#     def para_cekme(hesap):
#         with open("account_logs.txt","r+",encoding="utf-8") as file:
            
#             # for lines in file:
#             cekilecek_tutar = int(input("ne kadar çekeceksiniz: "))
#             if hesap["bakiye"]< cekilecek_tutar:
#                 print("yetersiz bakiyeeeeee!!!!!!!!!!!")
#                 return banka_hesap.menu(hesap) 
#             elif hesap["bakiye"]> cekilecek_tutar:      
#                 hesap["bakiye"]-=cekilecek_tutar
#                 return banka_hesap.menu(hesap)
#             else:
#                 print("hatalı girş ")
            
            
#     def para_yatir(hesap):
#         yatirilicak_tutar = int(input("ne kadar yatıracaksınız: "))
#         hesap["bakiye"] += yatirilicak_tutar
#         banka_hesap.menu(hesap)        
            
#     def menu(hesap):
#         islem = input(f"merhaba {hesap["hesapSahibi"]}\nhesap bakiyenin {hesap["bakiye"]}\n1-para yatırma\n2-para çekme\nseçim yapınız: ")
        
#         if islem == "1":
#             return banka_hesap.para_yatir(hesap) 
#         elif islem == "2":
#             return banka_hesap.para_cekme(hesap)   



# name = input("kullanıcı adı giriniz")
# password = input("şifre giriniz")

# for hesap in hesaplar:
        
#     if (hesap["kullaniciadi"] ==name  and password == hesap["password"]):
#         banka_hesap.menu(hesap)

#         break
#     else:
#         print(f"hatalı giriş  ")
    
    
    

# p1 = banka_hesap("sefa şeker",3033)


# sonuc = p1.bakiye

# print(sonuc)
# print(p1)

user_name = input("username: ")
sifre = input("password: ")

class Hesap_bilgileri :
    
    
    
    def para_yatirma(self):
        miktar = int(input("yatırılacak tutar: "))
        self.bakiye += miktar
        return Hesap_bilgileri.dogrulama(self)
        
        
        pass
    
    def para_cekme(self):
        miktar = int(input("yatırılacak tutar: "))
        self.bakiye -= miktar
        return Hesap_bilgileri.dogrulama(self)
        
        pass
    
    
    
    def __init__(self):
        self.username = "sefasekerr"
        self.password = "Pekmez1526"
        self.name = "Sefa "
        self.surname = "Şeker"
        self.bakiye = 45000
        
            
    def dogrulama(self):
        
        if  user_name == self.username and sifre == self.password:
            islem = input(f"merhaba {self.name} {self.surname}\nhesap bakiyeniz: {self.bakiye}\n1-para yatırma\n2-para çekme\n3-çıkış\nseçim: ") 
            if islem == "1":
                Hesap_bilgileri.para_yatirma(self)
            elif islem == "2":
                Hesap_bilgileri.para_cekme()
        
        
        else :
            print("hatalı giriş!!!!!!")
                        
       
        
        
hesap = Hesap_bilgileri()
hesap.dogrulama()




# print(Hesap_bilgileri.info())













