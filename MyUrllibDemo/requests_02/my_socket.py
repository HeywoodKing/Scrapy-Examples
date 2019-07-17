# -*- coding: utf-8 -*-


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('https://www.meizitu.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.meizitu.com\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close()

with open('meizi.html', 'wb') as f:
    f.write(data)

