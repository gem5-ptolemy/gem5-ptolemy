#ifndef __PARAMS__TsunamiCChip__
#define __PARAMS__TsunamiCChip__

class TsunamiCChip;

#include <cstddef>
#include "params/Tsunami.hh"

#include "params/BasicPioDevice.hh"

struct TsunamiCChipParams
    : public BasicPioDeviceParams
{
    TsunamiCChip * create();
    Tsunami * tsunami;
};

#endif // __PARAMS__TsunamiCChip__
