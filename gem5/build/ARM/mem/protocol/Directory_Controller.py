from m5.params import *
from m5.SimObject import SimObject
from Controller import RubyController

class Directory_Controller(RubyController):
    type = 'Directory_Controller'
    cxx_header = 'mem/protocol/Directory_Controller.hh'
    directory = Param.RubyDirectoryMemory("")
    memBuffer = Param.MemoryControl("")
    directory_latency = Param.Cycles(12, "")
