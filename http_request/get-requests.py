import requests
import chess

url = "https://weather-api167.p.rapidapi.com/api/weather/forecast"

querystring = {"place":"London,GB","cnt":"3","units":"standard","type":"three_hour","mode":"json","lang":"en"}

headers = {
	"x-rapidapi-host": "weather-api167.p.rapidapi.com",
	"Accept": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

board = chess.Board()

# Tahtayı yazdır
print(board)

# Geçerli hamleleri listele
print(list(board.legal_moves))

# Hamle yap (örneğin e4)
board.push_san("e4")

# Rakip hamlesi
board.push_san("e5")
print(board)


# Mat kontrolü
# print(board.is_checkmate())

