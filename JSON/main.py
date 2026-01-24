from login import*
from register import *
from secenek import oyun_secimi
def main():
    print(f".............OYUNUMUZA HOŞGELDİNİZ............")
    print(f"{'HESABINIZ VAR MI (R)':<15} ya da {'HESAP OLUŞTURUN (L)':>15}")
    sonuc =input("hangisi: ")
    if sonuc=="L" or sonuc=="l":
        name = input("isminizi giriniz: ")
        surname = input("soyisminizi giriniz: ")
        skor = ""
        user= Register(name,surname,skor)
        print("ARAMIZA HOŞGELDİNN!!\n")
        oyun_secimi()
        return user.as_tuple()
    elif sonuc=="R" or sonuc=="r":
        user_id,user_info=Login.login_control()
        oyun_secimi()
        return user_id,user_info
    # print(f"HOŞGELDİN ÖZLETME FAZLA:) {user[1]["name"].upper()}\n")
    else :
        print("hatalı tuşlama")
        return False

main()
    
