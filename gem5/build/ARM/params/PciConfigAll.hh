#ifndef __PARAMS__PciConfigAll__
#define __PARAMS__PciConfigAll__

class PciConfigAll;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/Platform.hh"

#include "params/BasicPioDevice.hh"

struct PciConfigAllParams
    : public BasicPioDeviceParams
{
    PciConfigAll * create();
    uint8_t bus;
    uint32_t size;
    Platform * platform;
};

#endif // __PARAMS__PciConfigAll__
