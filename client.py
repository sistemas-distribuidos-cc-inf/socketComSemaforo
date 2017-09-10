#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
from scbl import BufferLimitado

b = BufferLimitado()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
sock.connect(('127.0.0.1', port))
tamanhoAtualBuffer = b.cheio #opcional
print tamanhoAtualBuffer #opcional

def consumidor():
    while True:
      time.sleep(2)
      item = b.remove()
      print " CONSUMIDOR. item: ", item, " b.livre: ", b.livre, " b.cheio: ",  b.cheio

consumidor()

#sock.close()

