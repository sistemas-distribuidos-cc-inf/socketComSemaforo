#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

arr = ['Tuco', 'Bebel', 'Lineu', 'Agostinho', 'Paulão', 'Nene', 'Floriano', 'Beiçola', 'Marilda']
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1235
conn = sock.connect(('127.0.0.1', port))
sock.send('Consumir')
res = conn.recv(1024)
print 'resposta: ' + res

while 1: pass