import requests as rq
from bs4 import BeautifulSoup as bs
from csv import writer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

url = 'https://www.btkakademi.gov.tr/portal/catalog?categoryId=353'

driver.get(url)

html = driver.page_source
soup = bs(html, "html.parser")

obj = bs(soup.text,"html.parser")

sonuc = obj.find("gbt_catalog-main-right-course")

print(sonuc)

