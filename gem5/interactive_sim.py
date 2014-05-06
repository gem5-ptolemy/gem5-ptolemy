#! /usr/bin/env python

import os
import sys
from subprocess import Popen, PIPE
import shlex

sim = "./build/ARM/gem5.opt"
sim_opt = " --debug-start=1" + " --debug-flags=DRAM"#RubyMemory"#",Bus,Cache"

conf = " ./configs/example/interactive.py"
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

exe = " -c $MIBENCH_BIN/consumer/jpeg/cjpeg"
exe += " -o \"-dct int -progressive -opt -outfile $MIBENCH_BIN/consumer/jpeg/output_large_encode.jpeg $MIBENCH_BIN/consumer/jpeg/input_large.ppm\""

#exe = " -c $MIBENCH_BIN/security/rijndael/rijndael"
#exe += " -o \"$MIBENCH_BIN/security/rijndael/input_large.asc $MIBENCH_BIN/security/rijndael/output_large.enc \
# e 1234567890abcdeffedcba09876543211234567890abcdeffedcba0987654321\""


#exe = " -c $MIBENCH_BIN/consumer/typeset/lout"
#exe += " -o \"-I $MIBENCH_BIN/consumer/typeset/include -D $MIBENCH_BIN/consumer/typeset/data -F $MIBENCH_BIN/consumer/typeset/font \
#                -C $MIBENCH_BIN/consumer/typeset/maps -H $MIBENCH_BIN/consumer/typeset/hyph $MIBENCH_BIN/consumer/typeset/small.lout\""

#exe = " -c $MIBENCH_BIN/network/dijkstra/dijkstra_large"
#exe += " -o \"$MIBENCH_BIN/network/dijkstra/input.dat\""

#exe = " -c $MIBENCH_BIN/network/patricia/patricia"
#exe += " -o \"$MIBENCH_BIN/network/patricia/large.udp\""

#exe = " -c $MIBENCH_BIN/automotive/basicmath/basicmath_large"

#exe = " -c $MIBENCH_BIN/consumer/jpeg/djpeg"
#exe += " -o \"-dct int -ppm -outfile $MIBENCH_BIN/consumer/jpeg/output_small_decode.ppm $MIBENCH_BIN/consumer/jpeg/input_small.jpg\""
                
#exe = " -c $MIBENCH_BIN/office/stringsearch/search_small"

#exe = " -c $MIBENCH_BIN/automotive/susan/susan',
#exe += " -o \"$MIBENCH_BIN/automotive/susan/input_large.pgm $MIBENCH_BIN/automotive/susan/output_large.smoothing.pgm -s\""

print 'starting the simulation!!!'

#line = sys.stdin.readline()
os.system(sim + sim_opt + conf + conf_opt +  exe)
#args= shlex.split(sim + sim_opt + conf + conf_opt +  exe)
#Popen(args)

