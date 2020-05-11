import socket

HOST = '127.0.0.1'
PORT =  65432

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind((HOST, PORT))
mysock.listen()
conn, addr = mysock.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
mysock.close()    




