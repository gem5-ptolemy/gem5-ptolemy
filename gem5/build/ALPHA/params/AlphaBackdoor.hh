#ifndef __PARAMS__AlphaBackdoor__
#define __PARAMS__AlphaBackdoor__

class AlphaBackdoor;

#include <cstddef>
#include "params/Terminal.hh"
#include <cstddef>
#include "params/Platform.hh"
#include <cstddef>
#include "params/SimpleDisk.hh"
#include <cstddef>
#include "params/AlphaSystem.hh"
#include <cstddef>
#include "params/BaseCPU.hh"

#include "params/BasicPioDevice.hh"

struct AlphaBackdoorParams
    : public BasicPioDeviceParams
{
    AlphaBackdoor * create();
    Terminal * terminal;
    Platform * platform;
    SimpleDisk * disk;
    AlphaSystem * system;
    BaseCPU * cpu;
};

#endif // __PARAMS__AlphaBackdoor__
