# -*- coding: ISO-8859-1 -*-
import thread
import time, random
import threading

class BufferLimitado:
   TAM_BUFFER = 25
   mutex  = threading.Semaphore(1)
   empty  = threading.Semaphore(TAM_BUFFER)
   full   = threading.Semaphore(20)
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


