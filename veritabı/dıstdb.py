from database import Database

ilces =('ADALAR','ARNAVUTKÖY','ATAŞEHİR','AVCILAR','BAĞCILAR','BAHÇELİEVLER','BAKIRKÖY','BAŞAKŞEHİR','BAYRAMPAŞA','BEŞİKTAŞ','BEYKOZ','BEYLİKDÜZÜ','BEYOĞLU','BÜYÜKÇEKMECE','ÇATALCA','ÇAYIROVA','ÇEKMEKÖY','ESENLER','ESENYURT','EYÜP','EYÜPSULTAN','FATİH','GAZİOSMANPAŞA','GÜNGÖREN','KADIKÖY','KAĞITHANE','KAPAKLI','KARTAL','KÜÇÜKCEKMECE','KÜÇÜKÇEKMECE','MALTEPE','MERKEZ','PENDİK','SANCAKTEPE','SARIYER','SİLİVRİ','SULTANBEYLİ','SULTANGAZİ','ŞİLE','ŞİŞLİ','TUZLA','ÜMRANİYE','ÜSKÜDAR','YEŞİLKÖY','ZEYTİNBURNU')

databse = Database.get_connection()
cursor = databse.cursor()



sql = "INSERT INTO DISTRICTS (DISTRICT_NAME , CITY_ID) VALUES (?,34)"

cursor.executemany(sql,((ilce,) for ilce in ilces))
databse.commit()
print("eklendi")