import db 



def urun_guncelle(urunadi,fiyat,id):
    for urun in db.urunler:
        if urun["id"] == id :
            urun["urunadi"] =urunadi
            urun["fiyat"]= fiyat
            break
    else:
        print("a")       
        
    

def urun_ekle(urunadi,fiyat):
    db.urunler.append({
        "id":len(db.urunler)+1,
        "urunadi":urunadi,
        "fiyat":fiyat
    })
    
    
    

def urunleri_goruntule():
    return db.urunler
    