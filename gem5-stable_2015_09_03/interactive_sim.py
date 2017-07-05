#! /usr/bin/env python

import os
import sys
from subprocess import Popen, PIPE
import shlex

sim = "./build/ARM/gem5.opt"
sim_opt = " --debug-start=1" + " --debug-flags=DRAM"#RubyMemory"#",Bus,Cache"
sim_opt += " --interactive"

conf = " ./configs/example/interactive_se.py"
conf_opt = ""
#max_tick = 100000000
#conf_opt = " --checkpoint-at-end" + " --rel-max-tick=" + str(max_tick)
#conf_opt = " --rel-max-tick=" + str(max_tick)
#conf_opt += " --cpu-type=arm_detailed"
conf_opt += " --cpu-type=TimingSimpleCPU"
conf_opt += " --cpu-clock=1GHz --sys-clock=1GHz"
conf_opt += " --caches"
conf_opt += " --l1i_size=16kB --l1d_size=16kB"
#conf_opt += " --l2cache --l2_size=128kB"
conf_opt += " --mem-type=DDR3_1600_x64"
#conf_opt += " --ruby"

#exe = " -c ../wcet_bench/matmult.o"


exe = " -c ../MiBench/consumer/jpeg/jpeg-6a/cjpeg"
exe += " -o \"-dct int -progressive -opt -outfile ../MiBench/consumer/jpeg/output_large_encode.jpeg ../MiBench/consumer/jpeg/input_large.ppm\""


#exe = " -c ../MiBench/security/rijndael/rijndael"
#exe += " -o \"../MiBench/security/rijndael/input_large.asc ../MiBench/security/rijndael/output_large.enc \
# e 1234567890abcdeffedcba09876543211234567890abcdeffedcba0987654321\""


#exe = " -c ../MiBench/consumer/typeset/lout-3.24/lout"
#exe += " -o \"-I ../MiBench/consumer/typeset/lout-3.24/include -D ../MiBench/consumer/typeset/lout-3.24/data -F ../MiBench/consumer/typeset/lout-3.24/font \
#                -C ../MiBench/consumer/typeset/lout-3.24/maps -H ../MiBench/consumer/typeset/lout-3.24/hyph ../MiBench/consumer/typeset/small.lout\""


#exe = " -c ../MiBench/network/dijkstra/dijkstra_large"
#exe += " -o \"../MiBench/network/dijkstra/input.dat\""


#exe = " -c ../MiBench/network/patricia/patricia"
#exe += " -o \"../MiBench/network/patricia/large.udp\""


#exe = " -c ../MiBench/automotive/basicmath/basicmath_large"

#exe = " -c ../MiBench/consumer/jpeg/djpeg"
#exe += " -o \"-dct int -ppm -outfile ../MiBench/consumer/jpeg/output_small_decode.ppm ../MiBench/consumer/jpeg/input_small.jpg\""
                
#exe = " -c ../MiBench/office/stringsearch/search_small"

#exe = " -c ../MiBench/automotive/susan/susan',
#exe += " -o \"../MiBench/automotive/susan/input_large.pgm ../MiBench/automotive/susan/output_large.smoothing.pgm -s\""

print 'starting the simulation!!!'

#line = sys.stdin.readline()
os.system(sim + sim_opt + conf + conf_opt +  exe)
#args= shlex.split(sim + sim_opt + conf + conf_opt +  exe)
#Popen(args)

