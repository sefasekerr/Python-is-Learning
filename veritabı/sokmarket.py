from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://kurumsal.sokmarket.com.tr/magazalarimiz")

time.sleep(3)

# İl dropdown'unu bul ve İstanbul'u seç
il_dropdown = driver.find_element(By.ID, 'subeili')
select_il = Select(il_dropdown)
select_il.select_by_visible_text("İSTANBUL")

time.sleep(2)  # ilçelerin yüklenmesini bekle

# İlçe dropdown'unu bul ve örneğin 'GAZİOSMANPAŞA' seç
ilce_dropdown = driver.find_element(By.ID, 'subeilce')
select_ilce = Select(ilce_dropdown)
select_ilce.select_by_visible_text("GAZİOSMANPAŞA")

time.sleep(2)  # mağaza listeleme butonunun aktifleşmesini bekle

# Görüntüle butonuna bas
btn = driver.find_element(By.ID, 'btnSubeListele')
btn.click()

time.sleep(3)  # mağazaların yüklenmesini bekle

# Mağaza listelerini çek
magazalar = driver.find_elements(By.CLASS_NAME, "baslikTxt")
links = driver.find_elements(By.CLASS_NAME, "maplink")

# for link in links:
#     lat_attr = link.get_attribute("data-lng")
#     lon_attr = link.get_attribute("data-ltd")
#     print("RAW:", lat_attr, lon_attr)
geo_links = driver.find_elements(By.CLASS_NAME, "geolink")

for link in geo_links:
    href = link.get_attribute("href")
    if href and "daddr=" in href:
        coords = href.split("daddr=")[1]
        lat, lon = coords.split(",")
        print(f"Koordinat: {lat}, {lon}")

# for ad, link in zip(magazalar,links):
#     lat = link.get_attribute("data-lng")
#     lon = link.get_attribute("data-ltd")
#     if lat and lon:
#         lat = float(link.get_attribute("data-lng"))
#         lon = float(link.get_attribute("data-ltd"))
#     # print(f"Koordinat: {lat:.6f}, {lon:.6f}")

#         print(f"{ad.text} - -> Koordinat: {lat:.6f}, {lon:.6f}")
