import requests
from bs4 import BeautifulSoup
import csv

url ="https://www.trendyol.com/xbox-series-x-y-s12859"

response = requests.get(url)


soup = BeautifulSoup(response.text,"html.parser")
sonuc = soup.find(class_="search-result-content").find_all(class_="product-card")
with open("fiyatlar.csv","w",encoding="utf-8") as file:
    csv_writer= csv.writer(file)
    csv_writer.writerow(["link","img","name","price"])
    for anchor in sonuc:
        link = anchor.get("href")
        img = anchor.img.get("src")
        name = anchor.find(class_="product-name").text # get_next(strip=True)  bu da kullanılabilir
        price = anchor.find(class_="single-price").string if anchor.find(class_="single-price")!= None else anchor.find(class_="strikethrough-price").string
        print(price.string)

        csv_writer= csv.writer(file)
        csv_writer.writerow([link,img,name,price])
    # if price==None:
    #     price = anchor.find(class_="strikethrough-price")
    #     print(price.string)

    # else:
    #     print(price.string)
        
    tit = link
