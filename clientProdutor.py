#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

arr = ['Tuco', 'Bebel', 'Lineu', 'Agostinho', 'Paulão', 'Nene', 'Floriano', 'Beiçola', 'Marilda']
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1235
conn = sock.connect(('127.0.0.1', port))
tamArr = len(arr)
while tamArr > 0:
    print arr.pop()
    #sock.send('Produzir ' + arr.pop())
    #sock.send('Produzir ' + arr.pop())
    tamArr = len(arr)

while 1: pass