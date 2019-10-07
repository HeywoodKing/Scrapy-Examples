# -*- coding: utf-8 -*-


import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'ha', ('127.0.0.1', 8090))

print(s.recv(1024).decode('utf-8'))

s.close()
