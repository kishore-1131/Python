import socket

HOST = '127.0.0.1'
PORT =  65432

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'Hello I am your client')
data = mysock.recv(1024)

print("Recieved:", repr(data))
mysock.close()
