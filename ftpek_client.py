import socket
s = socket.socket()
host = input("ip serwera: ")
port = 3456
s.connect((host, port))
print("connected... ")
filename = input(str("pliczek nejmiczek daj: "))
filek = open(filename, 'wb')
file_dat = s.recv(1024000000)
filek.write(file_dat)
filek.close()
print("poszło")
