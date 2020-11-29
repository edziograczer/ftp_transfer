import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("daj ip twoje: ")
port = 3456
s.bind((host, port))
s.listen(1)
print("czekaj... ")
conn, addr = s.accept()
print(addr, "connected")
filename = input(str("daj nazwe pliku: "))
filek = open(filename, "rb")
filek_sender = filek.read(10240000)
conn.send(filek_sender)
print("no i git ")
