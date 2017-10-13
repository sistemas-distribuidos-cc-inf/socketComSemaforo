#!/usr/bin/python
# -- coding: utf-8 --

import socket
import thread
import threading
from multiprocessing import Queue
from threading import Thread
from scbl import BufferLimitado

b = BufferLimitado()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket criado"

port = 1235
sock.bind(('127.0.0.1', port))
print "Socket associado à porta %s" %(port)

sock.listen(5)
print "Socket está rodando"

queue = Queue() 

def produzir(item):
    b.insert(item)
    print "PRODUTOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ", b.cheio

def consumidor(self):
    item = b.remove()
    queue.put(item)
    print " CONSUMIDOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ",  b.cheio

while 1:
    conn, addr = sock.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    msg = conn.recv(1024)
    arrAcao = msg.split()
    acao = arrAcao[0]
    print 'Ação: ' + acao
    item = arrAcao[1]
    #print 'Item: ' + item
    if acao == 'Produzir':
        thread.start_new_thread(produzir, (item, ))
    elif acao == 'Consumir':
        thread_ = threading.Thread(target=consumidor, args=(item, ))
        thread_.start()
        thread_.join()
        conn.send(queue.get())