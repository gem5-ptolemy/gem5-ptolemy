#! /usr/bin/env python

import os
import sys

fifo_name = 'test_fifo'
#os.mkfifo(fifo_name)

fifo = os.open(fifo_name, os.O_WRONLY)
print 'starts'
i = 0
a = 'abc'
while True:
  os.write(fifo,'hokeun: ' + a + '\n')
  a = sys.stdin.readline()
  print a

