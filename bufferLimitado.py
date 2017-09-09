# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading

class BufferLimitado:
   TAM_BUFFER = 10
   mutex  = threading.Semaphore(1)
   empty  = threading.Semaphore(TAM_BUFFER)
   full   = threading.Semaphore(0)
   buffer = range(TAM_BUFFER)
   cheio  = 0
   livre  = 0

   def insert(self, item):
      self.empty.acquire()
      self.mutex.acquire()
      self.buffer[self.livre] = item
      self.livre = (self.livre + 1) % self.TAM_BUFFER
      self.mutex.release()
      self.full.release()

   def remove(self):
      self.full.acquire()
      self.mutex.acquire()
      item = self.buffer[self.cheio]
      self.cheio = (self.cheio + 1) % self.TAM_BUFFER
      self.mutex.release()
      self.empty.release()
      return item

b = BufferLimitado()

def produtor():
   item = 0
   while True:
      time.sleep(2)
      item = item + 1
      b.insert(item)
      print "PRODUTOR. item: ", item, " b.livre: ", b.livre, " b.cheio: ", b.cheio
      print "_________________"

def consumidor():
   while True:
      time.sleep(2)
      item = b.remove()
      print "CONSUMIDOR. item: ", item, " b.livre: ", b.livre, " b.cheio: ",  b.cheio
      print "_________________"

thread.start_new_thread(produtor, ())
thread.start_new_thread(consumidor, ())

while 1: pass