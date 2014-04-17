import optparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath, fatal

addToPath('../common')
addToPath('../ruby')
addToPath('../topologies')

import Options
from m5.objects import *
from Caches import *
import Simulation

parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)
(options, args) = parser.parse_args()

if options.cmd:
    print >> sys.stdout, "Workload specified.\n"
else:
    print >> sys.stderr, "No workload specified. Exiting!\n"
    sys.exit(1)

workloads = options.cmd.split(';')

multiprocesses = []
idx = 0
for wrkld in workloads:
    process = LiveProcess()
    process.executable = wrkld
    process.cwd = os.getcwd()
    process.cmd = [wrkld]
    multiprocesses.append(process)
    idx += 1

#cpu = TimingSimpleCPU(cpu_id = 0)
cpu = AtomicSimpleCPU(cpu_id = 0)

(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
system = System(cpu = cpu,
#mem_mode = test_mem_mode,
        pysmem = SimpleMemory(),
        membus = NoncoherentBus())

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
    voltage_domain = system.voltage_domain)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
        voltage_domain = system.cpu_voltage_domain)

#cpu.addPrivateSplitL1Caches(O3_ARM_v7a_ICache, O3_ARM_v7a_DCache)
system.cpu.addPrivateSplitL1Caches(L1Cache(size = '4kB'), L1Cache(size = '4kB'))
system.cpu.connectAllPorts(system.membus)
system.cpu.createInterruptController()
# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
# for icpu in system.cpu:
cpu.clk_domain = system.cpu_clk_domain

system.cpu.workload = multiprocesses[0]
system.system_port = system.membus.slave

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)


