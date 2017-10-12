#!/usr/bin/python
# -- coding: utf-8 --

import socket
import thread
from Queue import Queue
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

def produzir(item):
    b.insert(item)
    print "PRODUTOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ", b.cheio

def consumidor(self):
    item = b.remove()
    print " CONSUMIDOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ",  b.cheio
    return item

item = Queue(maxsize=0)

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
        res = Thread(target=consumidor, args=(item,))
 	res.setDaemon(True)
 	res.start()
        resStr = str(res)
        print 'res: ' + resStr
        conn.send(resStr)
