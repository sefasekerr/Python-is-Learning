# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select,WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import time

# driver = webdriver.Chrome()

# driver.get("https://kurumsal.sokmarket.com.tr/magazalarimiz")

# time.sleep(1)

# il_dropdown = driver.find_element(By.ID, 'subeili')
# select_il = Select(il_dropdown)
# select_il.select_by_visible_text("İSTANBUL")

# time.sleep(1)
# ilce_dropdown = driver.find_element(By.ID, 'subeilce')
# select_ilce = Select(ilce_dropdown)

# wait = WebDriverWait(driver, 10)
# ilce_dropdown = wait.until(
#     EC.presence_of_element_located((By.ID, "subeilce"))
# )



# ilceler = [opt.text for opt in select_ilce.options if opt.text.strip() != ""]
# print(ilceler)


# ilceler=[]
# for i in select_ilce.options:
#     sonuc = i.text
#     ilceler.append(sonuc)
#     # print(i.text)
    
# print(ilceler)
towns = {"ADALAR" : 1	,
"ARNAVUTKÖY" : 2	,
"ATAŞEHİR" : 3	,
"AVCILAR" : 4	,
"BAĞCILAR" : 5	,
"BAHÇELİEVLER" : 6	,
"BAKIRKÖY" : 7	,
"BAŞAKŞEHİR" : 8	,
"BAYRAMPAŞA" : 9	,
"BEŞİKTAŞ" : 10,
"BEYKOZ" : 11,
"BEYLİKDÜZÜ" : 12,
"BEYOĞLU" : 13,
"BÜYÜKÇEKMECE" : 14,
"ÇATALCA" : 15,
"ÇAYIROVA" : 16,
"ÇEKMEKÖY" : 17,
"ESENLER" : 18,
"ESENYURT" : 19,
"EYÜP" : 20,
"EYÜPSULTAN" : 21,
"FATİH" : 22,
"GAZİOSMANPAŞA" : 23,
"GÜNGÖREN" : 24,
"KADIKÖY" : 25,
"KAĞITHANE" : 26,
"KAPAKLI" : 27,
"KARTAL" : 28,
"KÜÇÜKCEKMECE" : 29,
"KÜÇÜKÇEKMECE" : 30,
"MALTEPE" : 31,
"MERKEZ" : 32,
"PENDİK" : 33,
"SANCAKTEPE" : 34,
"SARIYER" : 35,
"SİLİVRİ" : 36,
"SULTANBEYLİ" : 37,
"SULTANGAZİ" : 38,
"ŞİLE" : 39,
"ŞİŞLİ" : 40,
"TUZLA" : 41,
"ÜMRANİYE" : 42,
"ÜSKÜDAR" : 43,
"YEŞİLKÖY" : 44,
"ZEYTİNBURNU" : 45,}
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
from database import Database

data = Database.get_connection()

cursor = data.cursor()
koordinatlar={}
def ilce_save(ilce):
    driver = webdriver.Chrome()
    driver.get("https://kurumsal.sokmarket.com.tr/magazalarimiz")
    time.sleep(1)

    il_dropdown = driver.find_element(By.ID, 'subeili')
    Select(il_dropdown).select_by_visible_text("İSTANBUL")
    time.sleep(5)


    ilce_dropdown = driver.find_element(By.ID, 'subeilce')
    Select(ilce_dropdown).select_by_visible_text(ilce)
    time.sleep(2)
    
    driver.find_element(By.ID,'btnSubeListele').click()
    time.sleep(5)
    
    magazalar =  driver.find_elements(By.CSS_SELECTOR,"div#dummybayi")
    time.sleep(3)
    distirict_id=towns.get(ilce)
    
    koor_list=[]
    sql = "INSERT INTO STORES (STORE_NAME, STORE_COUNTRY_ID, STORE_CITY_ID, STORE_DISTRICT_ID, STORE_LTD, STORE_LNG)VALUES (?,1,34,?,?,?)"
    for magaza in magazalar:
        baslik = magaza.find_element(By.CSS_SELECTOR,"h4.baslikTxt").text.strip()
        link = magaza.find_element(By.CSS_SELECTOR,"a.geolink").get_attribute("href")
        if link and "daddr="in link:
            lat,lon = link.split("daddr=")[1].split(",")
            koor_list.append(f"{baslik:<43}=koordinat:{lat.strip()},{lon.strip()}")
            # cursor.execute(sql,(baslik,distirict_id,float(lat),float(lon)))
            # data.commit()
    koordinatlar[ilce]=koor_list  
    driver.close()      
    
    #dummybayi   mağazadetayları bu id saklanıyor detayları 
    

    

    
    

threads = []
for ilce,plaka in towns.items():

    t = threading.Thread(target=ilce_save,args=(ilce,))
    threads.append(t)
    t.start()
    time.sleep(5)
    
for t in threads:
    t.join()


with open("koordinatlar.txt","w",encoding="utf-8")as file:
        for ilc,koord in koordinatlar.items():
            for a in koord:
                file.write(f"{ilc}->{towns.values()}{a}\n")


print("koordinatlar kaydedildi")  


