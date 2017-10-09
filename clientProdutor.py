#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time

millis = str(time.time())
#itemstr = str(item)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1235
conn = sock.connect(('127.0.0.1', port))
sock.send('Produzir ' + millis)