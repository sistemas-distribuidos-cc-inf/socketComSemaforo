#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import thread
import time
from scbl import BufferLimitado

b = BufferLimitado()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
sock.connect(('127.0.0.1', port))


while 1: pass