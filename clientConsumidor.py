#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1235
conn = sock.connect(('127.0.0.1', port))
sock.send('Consumir 0')
res = conn.recv(1024)
print 'resposta: ' + res

while 1: pass