
try:

    class Hesap_Makinesi():

        def toplam(a,b):            
            return a+b
        
        def cikarma(a,b):
            return a- b
        
        def carpma(a,b):
            return a*b
        
        def bolme(a,b):
            if b ==0:
                raise ZeroDivisionError ("sıfıra bölme hatası")
            return a/b
        
        
except Exception as ex:
    hatalar = []
    hatalar.append(f"{ex}\n")
    with open("hatalar.txt","r+",encoding="utf-8")as f:
        for hata in hatalar:
            f.write(hata)
    print(ex)