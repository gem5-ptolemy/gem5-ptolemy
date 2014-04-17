#ifndef __PARAMS__TsunamiPChip__
#define __PARAMS__TsunamiPChip__

class TsunamiPChip;

#include <cstddef>
#include "params/Tsunami.hh"

#include "params/BasicPioDevice.hh"

struct TsunamiPChipParams
    : public BasicPioDeviceParams
{
    TsunamiPChip * create();
    Tsunami * tsunami;
};

#endif // __PARAMS__TsunamiPChip__
