# -*- coding: utf-8 -*-


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8888))

buffer = []
d = s.recv(1024)
buffer.append(d)


data = b''.join(buffer)
print(data)

s.close()

