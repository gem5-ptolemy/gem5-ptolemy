#! /usr/bin/env python

import re

def count_mem_requests(file_name):
  f = open(file_name)
  isInit = True
  init_write_count = 0
  write_count = 0
  read_count = 0
  exit_tick = -1
  for line in f:
    if isInit:
      if 'system.mem_ctrls: Write' in line:
        init_write_count += 1
    else:
      if 'system.mem_ctrls: Write' in line:
        write_count += 1
      elif 'system.mem_ctrls: Read' in line or 'system.mem_ctrls: IFetch' in line:
        read_count += 1
      
    if 'REAL SIMULATION' in line:
      isInit = False
    elif 'Exiting @ tick' in line:
      sp = re.split(' *', line)
      if len(sp) > 3:
        exit_tick = int(sp[3])
  print '\tinit_writes:\t' + str(init_write_count),
  print '\twrites:\t' + str(write_count),
  print '\treads:\t' + str(read_count),
  print '\ttotal accesses:\t' + str(write_count + read_count),
  exit_tick = exit_tick / 500
  print '\tticks:\t' + str(exit_tick),
  if exit_tick > 0:
    print '\tmem intensity:\t' + str(100.0 * (write_count + read_count) / exit_tick),
  print ''

import sys

if len(sys.argv) <= 1:
  sys.exit('Error: input mem traces.')
  
trace_list = sys.argv
trace_list.remove(sys.argv[0])

for trace in sys.argv:
  sp = re.split('\.',trace)
  print sp[0],
  count_mem_requests(trace)
