#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import thread
import time
from random import randint
from scbl import BufferLimitado

b = BufferLimitado()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket criado"

port = 1235
sock.bind(('127.0.0.1', port))
print "Socket associado à porta %s" %(port)

sock.listen(5)
print "Socket está rodando"

def produzir():
    item = 0
    while True:
        time.sleep(0.5)
        item = randint(0, 1000)
        b.insert(item)
        print "PRODUTOR. item: ", item #, " b.livre: ", b.livre, " b.cheio: ", b.cheio

def consumidor():
    cont = 0
    while cont < 10:
        cont = cont + 1
        time.sleep(0.5)
        item = b.remove()
        print " CONSUMIDOR. item: ", item #, " b.livre: ", b.livre, " b.cheio: ",  b.cheio

thread.start_new_thread(produzir, ())


while 1:
    conn, addr = sock.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread.start_new_thread(consumidor, ()) 