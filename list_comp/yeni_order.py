from database import Database

database = Database.get_connection()
cursor = database.cursor()
sql_urunler="select * from items"
cursor.execute(sql_urunler)
items ={}
for id,name,price,stock in cursor.fetchall():
    items[id]=[name,price,stock]
    
print(items)

def menu_print():
    print(f"{'_'*9:<7}HOŞGELDİNİZ{'_'*10:>7}")
    for key,item in items.items():
        left =f"{"|":<5}{key}-{item[0]:<8}: {item[1]} {'TL':<2}"
        padding= 30-len(left)
        print(f"{left}{' '*padding}|")        
    secenek()
        
def secenek():
    total = []
    for i in range(3):
        secimler = int(input("hangi ürünlerden alacaksınız numarasını giriniz: "))
        miktar = int(input("kaç tane alacaksınız: "))
        if secimler <=len(items):
            total.append((secimler,miktar))
        else:
            print("hatalı seçim")
            
    total_price(total)
    # return total

def total_price(total):
    toplam = 0
    for a in total:
        ürün_id,quantitiy = a

        if stock_dus(ürün_id,quantitiy):
            for k in items.keys():
                if ürün_id == k:
                    fiyat = items.get(k)[1]
                    toplam += fiyat *quantitiy
        else:
            continue
    invoices(total,toplam)
    # return toplam

def stock_dus(item_id,quantity):
    sql = "UPDATE items SET item_stock=? where item_id=?"
    net = stock_varmi(item_id)-quantity
    
    if net >=0:
        cursor.execute(sql,(net,item_id))
        database.commit()
        return True
    else:
        print(f"{item_id} kodlu üründen stok kalmadı mevcut stok{stock_varmi(item_id)}")
        return False
    # print(cursor.fetchone())
        
        
def stock_varmi(ürün_id):
    sql = "select item_stock from items where item_id=?"
    cursor.execute(sql,(ürün_id,))
    database.commit()
    stok = cursor.fetchone()
    return stok[0]

def invoices(total,toplam):
    print(f"{'_'*3:<3}ŞEKER PASTANESİ{'_'*3:>3}")
    print(f"{"|":<21}|")
    for i in total:
        id_ürün , quantity = i
        ad,fiyat,stok = items.get(id_ürün)
        print(f"|{ad:<8}-{round(quantity*fiyat,2):<6} TL{"|":>3}")
    print(f"{"|":<21}|")
    print(f"{"|"} Toplam tutar: {toplam:<5}|")
    print(f"{"|":<21}|")
    
    
menu_print()
    



def urun_ekle():
    sql = "INSERT INTO items values (?,?,?)"
    name = input("ürün ismini giriniz : ")
    pric = float(input("fiyatı giriniz: "))
    stok = int(input("stoğu giriniz: "))
    cursor.execute(sql,(name,pric,stok))
    database.commit()
    print(f"{name} isimli ürün eklendi")
    
