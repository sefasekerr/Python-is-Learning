from urunler import urunler

toplam = 0
def urun_sorgula(urun_isim="kulaklık"):
    for urun in urunler:
        if urun["urun_adi"] == urun_isim :
            return f"ürünün id numarası: {urun["id"]}\nürünün ismi: {urun["urun_adi"]}\nürünün fiyatı: {urun['fiyat']}\nkalan stok: {urun['stok']}\n"

    
        
liste = []       
def fiyat_hesaplama(urun_isim=None,miktar=None): 
    urun_fiyati = 0
    
    for urun in urunler:
        if urun_isim == urun["urun_adi"]:
            liste.append(urun_isim)
            if urun['stok']>=miktar:
                urun_fiyati = urun['fiyat'] * miktar
                urun['stok'] -= miktar
                break
            else:
               return f"yetersiz stok"
        else:
            return f"ürün yok"
            
    return toplam_tutar(urun_fiyati)
    
def toplam_tutar(urun_fiyati):
    global toplam
    global liste
    
    toplam += urun_fiyati
    return f"{toplam} {liste}"

# def stok(miktar,urun_isim):
#     for urun in urunler:
#         if urun_isim == urun['stok']:
#             urun['stok'] -= miktar
#             break
# fiyat_hesaplama()
def urun_ekle(product_name,price,stock):
    urunler.append({
        "id":len(urunler)+1,
        "urun_adi":product_name,
        "fiyat":price,
        "stok":stock
    })