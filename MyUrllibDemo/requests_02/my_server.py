# -*- coding: utf-8 -*-


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8888))


s.listen(1)

while True:
    sock, addr = s.accept()
    print('有人连进来了')
    sock.send(b'hi man, are you ok?')
    sock.close()

