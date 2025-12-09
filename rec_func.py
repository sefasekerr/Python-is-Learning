# def sayi_listesi(sayi1,sayi2):
#     sayilar = [ i for i in range(sayi1,sayi2+1)]
#     return sayilar

# def asallar(start_num,finish_num):   
#     sonuc = []
#     for i in sayi_listesi(start_num,finish_num):
#         adet = 0
#         for a in range(2,i+1):
#             if i % a ==0:
#                 adet = adet +1
#         else :
#             if adet == 1:
#                 sonuc.append(f"sayi asaldir: {a}")
#                 adet =0,
#             else:
#                 adet = 0   
#     return print(sonuc)

# start_num = int(input('bailangıç sayısını giriniz: '))
# finish_num = int(input('bitiş sayısını giriniz: '))   
    
# asallar(start_num,finish_num)


# from moviepy import TextClip

# clip = TextClip("Merhaba Sefa!", fontsize=70, color="white", size=(640,480))
# clip = clip.set_duration(5)
# clip.write_videofile("test.mp4", fps=24)


import requests
from bs4 import BeautifulSoup

def get_tr_trends():
    url = "https://trends.google.com/trending?geo=TR"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "xml")
    items = soup.find_all("title")
    return [i.text for i in items[1:]] 
print(get_tr_trends())