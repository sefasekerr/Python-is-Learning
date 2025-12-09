""",
Bir market uygulaması yapıyorsun. Kullanıcı giriş yaptıktan sonra menüden şu işlemleri seçebiliyor:
- Ürünleri Listele
- Market rafındaki ürünleri ve fiyatlarını göster.
- Sepete Ürün Ekle
- Kullanıcı ürün adı ve miktar giriyor, sepete ekleniyor.
- Sepeti Görüntüle
- Sepetteki ürünleri ve toplam tutarı göster.
- Ödeme Yap
- Kullanıcı ödeme yapınca bakiye kontrol ediliyor.
- Eğer bakiye yeterliyse alışveriş tamamlanıyor, değilse “Yetersiz bakiye” uyarısı çıkıyor.
"""

urunler = {
    "elma":20,
    "armut":18,
    "muz":30,
    "karpuz":5,
    "kavun":8,
    "süt":25,
    "tavuk":80
}
# sepet_urunler = []
# sepet_miktar = []
# def alinan_urunler():
#     global sepet_urunler
#     global sepet_miktar
#     while True:
#         urun = input("aldığınız ürünü girin: ")
#         sepet_urunler.append(urun)
#         miktar = input("aldığınız ürünün miktarı: ")
#         sepet_miktar.append(miktar)

def hesapla():
    u = urunler.keys()
    aldigi_urunler = input("ne aldın: ")
    if aldigi_urunler in u:
        y = urunler[aldigi_urunler]
    return print(y)
        
    
hesapla()
   
    
    
    
    
    
    
# def urun(sepet):
    


