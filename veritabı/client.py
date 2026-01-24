import socket

PORT=12345
FORMAT = 'UTF-8'
BYTESIZE = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS=(SERVER,PORT)
DISSCONNECT_MESSAGE = "quit"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDRESS)

while True:
    message = client.recv(BYTESIZE).decode(FORMAT)
    
    if message ==DISSCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print("çıkış yapılıyor...")
        break
    else :
        message=input("mesaj: ")
        client.send(message.encode(FORMAT))
        
client.close()