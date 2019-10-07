# -*- coding: utf-8 -*-


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 8090))

while True:
    data, addr = s.recvfrom(1024)
    print(addr)
    s.sendto(b'hi man, are you ok?', addr)
