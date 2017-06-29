import socket
import time

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

playaz = []

print('Server Running')
while True:
    playerpos, addr = s.recvfrom(1024)
    if addr not in playaz:
        playaz.append(addr)
    for i in playaz:
        s.sendto(playerpos, i)
s.close()
