#! /usr/bin/env python

import os

fifo_name = 'test_fifo'
os.unlink(fifo_name)
os.mkfifo(fifo_name)

fifo = os.open(fifo_name, os.O_RDONLY)

while True:
  line = os.read(fifo, 100)
  print line

