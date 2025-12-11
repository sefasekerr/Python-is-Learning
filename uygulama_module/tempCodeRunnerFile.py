from methods import *

def menu():
    print(f"mağazaya hoşgeldiniz\n"
        f"1-yeni ürün ekleyebilirsiniz\n"
         
        f"2-ürün güncellemesi\n"
         
        f"3-ürünleri listeleyin")
    islem = input("ne yapacaksınız: ")
    #

    if islem =="1":
        urunadi = input("ürünün adını giriniz: ")