import socket

PORT=12345
FORMAT = 'UTF-8'
BYTESIZE = 1024
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS=(SERVER,PORT)
DISSCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print("server çalışıyor\n")

client_socket,client_address =server.accept()
client_socket.send("sunucu bağlantısı yapılıyor...\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)
    
    if message ==DISSCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print("çıkış yapılıyor...\n")
        break
    else :
        message = input("mesaj: ")
        client_socket.send(message.encode(FORMAT))
        
server.close()