from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Edge()
driver.get("https://www.btkakademi.gov.tr/portal/catalog?categoryId=35,353")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gbt_catalog-main-right-course"))
)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

sonuc = soup.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper")

# a = sonuc.find(title="Python Programlama ")
for kurs in sonuc:
    anchor = kurs.a
    img = anchor.find("img", attrs={ "alt":"STM32 ile Gömülü Yazılım Geliştirme İleri Seviye"})
    title = anchor.find(class_="font-medium text-base").string
    seviye = anchor.find
    # link = anchor.get("href")
    # if img == None:
    #     continue
    # else:
    #     print(img)
    print(title)