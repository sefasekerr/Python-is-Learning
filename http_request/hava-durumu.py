import requests
import json
from tkinter import *
# api_key = "4ef30ad7703f45a4a6f85706260401"
# url ="http://api.weatherapi.com/v1/current.json"
# konum = input("konum: ")
# # pencere=Tk()

# response = requests.get(url,params={
#     "key":api_key,
#     "q":konum,
#     "lang":"tr"
# })

# derece = response.json()["current"]["temp_c"]
# location = response.json()["location"]["tz_id"]
# icon = response.json()["current"]["condition"]["icon"]
# text = response.json()["current"]["condition"]["text"]
# # sonuc1 = sonuc
# # for i in sonuc:
# #     for x in i.keys():
# #         print(x)
# print(f"konum: {location},derece: {derece},yorum: {text}")
# print(icon)


import requests

url = "https://api.themoviedb.org/3/account/22620490/rated/movies?language=en-US&page=1&sort_by=created_at.asc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZGNmNTZmNTA1YzVmMjM3OTgxMDEzYmVlNGM0Y2ViYSIsIm5iZiI6MTc2NzUyMTE3OC41MDEsInN1YiI6IjY5NWEzYjlhZjliY2EwNzdlMjRhZmJlMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1F9E2Bvv7HAojgcHLbuFHaTGYVbAZsYrNsSLY90DwBY"
}

response = requests.get(url, headers=headers)

print(response.text)