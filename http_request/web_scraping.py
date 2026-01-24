from bs4 import BeautifulSoup as bs
import requests as rq

with open("index.html",encoding="utf-8") as file:
    html = file.read()
    # print(html)
    
# obj = BeautifulSoup(html,"html.parser")

# # sonuc = obj.prettify()
# sonuc = obj.title.string

# sonuc= obj.body.h2

# sonuc = obj.div

# sonuc = obj.contents
# print(sonuc)

# obj = bs(html,"html.parser")

# sonuc = obj.find_all("div")
# sonuc = len(obj.find_all("div"))
# sonuc = obj.find_all("div")[1].ul.find_all("li")[1]
# sonuc = obj.find_all("#")

# for div in obj.find_all("div"):
#     if div.h2.a != None:
#         print(div.h2.a.string.strip())
#     else:
#         print(div.h2.string.strip())
        
        
# for a in obj.find_all("a"):
#     print(a)
        
# print(sonuc)
# obj = bs(html,"html.parser")

# sonuc = obj.find(id="item1")

# sonuc = obj.find_all(class_="item")

# sonuc = obj.select("#header1")#
# sonuc = obj.select(".item")
# sonuc = obj.select_one(".item")

# sonuc= obj.find_all("div")

# # for i in sonuc:
# #     i = i.attrs["class"]
# #     print(i)
    
# sonuc = obj.ul.get_text(separator=" | ",strip=True)
# print(sonuc)

url = 'https://www.tcmb.gov.tr/kurlar/kurlar_tr.html'

response = rq.get(url)
response.encoding = response.apparent_encoding 

html_metni = response.text

result = bs(html_metni,"html.parser")
# # sonuc = sonuc.div.text
# sonuc = result.select_one('#kurlarTablo')
sonuc = result.find_all('body')[0].find_all("section")[0].find_all(id='data')
sonuc = result.find_all(id='data')

print(sonuc)
url = "https://www.tcmb.gov.tr/kurlar/today.xml"
response = rq.get(url)
soup = bs(response.content, "xml")

# Örnek: USD ve EUR çekelim
usd = soup.find("Currency", {"Kod":"USD"}).ForexSelling.text
eur = soup.find("Currency", {"Kod":"EUR"}).ForexSelling.text
# sonuc = soup.find_all("Currency")

print("USD:", usd)
print("EUR:", eur)
# print(sonuc)