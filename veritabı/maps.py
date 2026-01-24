import requests

API_KEY = "AIzaSyBUEk5V8x_cyHMdkHH0pc3pT51v7hbYiPE"
query = "Şok Market İstanbul"
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"

response = requests.get(url)
data = response.json()
print(len(data["results"]))
for place in data["results"]:
    name = place["name"]
    lat = place["geometry"]["location"]["lat"]
    lng = place["geometry"]["location"]["lng"]
    print(name, lat, lng)
