#ifndef __PARAMS__AmbaIntDevice__
#define __PARAMS__AmbaIntDevice__

class AmbaIntDevice;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/BaseGic.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/AmbaPioDevice.hh"

struct AmbaIntDeviceParams
    : public AmbaPioDeviceParams
{
    uint32_t int_num;
    BaseGic * gic;
    Tick int_delay;
};

#endif // __PARAMS__AmbaIntDevice__
