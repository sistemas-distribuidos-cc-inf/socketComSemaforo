#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from scbl import BufferLimitado

b = BufferLimitado()

sock = socket.socket()
port = 12345
sock.connect(('127.0.0.1', port))

#def consumidor():
#   while True:
#      time.sleep(2)
#      item = b.remove()
#      print "CONSUMIDOR. item: ", item, " b.livre: ", b.livre, " b.cheio: ",  b.cheio
#      print "_________________"
#

sock.close()
