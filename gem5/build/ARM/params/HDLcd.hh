#ifndef __PARAMS__HDLcd__
#define __PARAMS__HDLcd__

class HDLcd;

#include <cstddef>
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/VncInput.hh"

#include "params/AmbaDmaDevice.hh"

struct HDLcdParams
    : public AmbaDmaDeviceParams
{
    HDLcd * create();
    bool enable_capture;
    Tick pixel_clock;
    VncInput * vnc;
};

#endif // __PARAMS__HDLcd__
