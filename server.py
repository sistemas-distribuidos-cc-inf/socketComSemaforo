#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time
from scbl import BufferLimitado

b = BufferLimitado()
sock = socket.socket()
print "Socket criado"

port = 12345
tamanhoAtualBuffer = b.livre
sock.bind(('localhost', port))
print "Socket associado à porta %s" %(port)

sock.listen(5)
print "Socket está rodando"
print tamanhoAtualBuffer

def produzir():
    item = 0
    while tamanhoAtualBuffer < 10:
        time.sleep(2)
        item = item + 1
        b.insert(item)
        print "PRODUTOR. item: ", item, " b.livre: ", b.livre, " b.cheio: ", b.cheio

produzir()

while 1:
    conn, addr = sock.accept()
    conn.send('Thank you for connecting')
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

# sock.close()