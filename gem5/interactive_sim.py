#! /usr/bin/env python

import os

sim = "./build/ARM/gem5.opt"
sim_opt = " --debug-start=1" + " --debug-flags=Bus,Cache"

conf = " ./configs/example/interactive.py"
max_tick = 50000
#conf_opt = " --checkpoint-at-end" + " --rel-max-tick=" + str(max_tick)
conf_opt = " --rel-max-tick=" + str(max_tick)

exe = " -c ../wcet_bench/matmult.o"

os.system(sim + sim_opt + conf + conf_opt +  exe)

