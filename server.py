#!/usr/bin/python
# -*- coding: utf-8 -*-

# Socket Python Doc: https://docs.python.org/2.7/library/socket.html

# Importe o pacote do socket.
import socket

# Cria um objecto socket por padrão TCP/IP.
sock = socket.socket()
print "Socket successfully created"

# Reserve a porta na qual deseja aceitar conexões.
port = 12345

# Ative a porta para o servidor
sock.bind(('localhost', port))
print "Socket binded to %s" %(port)

# Coloque o socket no modo de listening (escuta de conexão).
sock.listen(5)
print "Socket is listening"

# Espere estabelecer conexão com um cliente.
conn, addr = sock.accept()
print 'Got connection from', addr

# Envie uma mensagem para o cliente.
#conn.send('Thank you for connecting')

#now keep talking with the client
count = 0
while 1:
    #wait to accept a connection - blocking call
    conn, addr = sock.accept()
    conn.send('Thank you for connecting')
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    count = count + 1
    print count 
    if count == 2:
        sock.close()