#! /usr/bin/env python

import os

sim = "./build/ARM/gem5.opt"
sim_opt = " --debug-flags=Bus,Cache"

conf = " ./configs/example/se.py"
max_tick = 10000
#conf_opt = " --checkpoint-at-end" + " --rel-max-tick=" + str(max_tick)
conf_opt = " --checkpoint-at-end" + " --maxinsts=" + "10"

exe = " -c ../wcet_bench/matmult.o"

os.system(sim + sim_opt + conf + conf_opt +  exe)

restore_cnt = 1

os.system(sim + sim_opt + conf + conf_opt + " -r " + str(restore_cnt) + exe)

restore_cnt = 2

os.system(sim + sim_opt + conf + conf_opt + " -r " + str(restore_cnt) + exe)

restore_cnt = 3

os.system(sim + sim_opt + conf + conf_opt + " -r " + str(restore_cnt) + exe)


