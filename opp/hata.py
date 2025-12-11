# liste = ["1","2","3","4","20b","10a","abc","60"]
# try:
# for i in liste:
#     try:
#         sonuc = int(i)
#         print(sonuc)
#     except:
#         continue
#except:

# liste = []
   
# while True:       
#     giris = input("giriş yapın: ")
#     if giris =="q":
#         print("a\n")
#         break
#     try:               
#         sonuc = float(giris)            
#         liste.append(sonuc)
#         print(sonuc)
            
#     except Exception as e :
#         liste.append(e)
#         with open("hatalar.txt","r+",encoding="utf-8") as f:
#             for hata in liste:
#                 f.writelines(f"{hata}\n")
#         print("sayı girişi yapınn")
#         print(e)



def fonksiyon(x):
    try:
        if x == 0:
            
            raise Exception ("x 0 veya daha küçük olmaz")
            
        else: 
            if x == 1:
                return 1
                
            else:
                return x * fonksiyon(x-1)
    except Exception as ex:
        print(ex)
   
   
print(fonksiyon(0))


prola = input("şifre girin : ")





















  





