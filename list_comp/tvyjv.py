from database import Database

database = Database.get_connection()
cursor = database.cursor()
sql_urunler="select * from items"
cursor.execute(sql_urunler)
items ={}
for id,name,price,stock in cursor.fetchall():
    items[id]=[name,price,stock]

sql = "select item_stock from items where item_id=?"
cursor.execute(sql,(3,))
database.commit()
stok = cursor.fetchone()

print(stok[0])
