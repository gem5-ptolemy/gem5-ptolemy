#ifndef __PARAMS__Pl011__
#define __PARAMS__Pl011__

class Pl011;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/BaseGic.hh"
#include <cstddef>
#include <cstddef>
#include "base/types.hh"

#include "params/Uart.hh"

struct Pl011Params
    : public UartParams
{
    Pl011 * create();
    uint32_t int_num;
    BaseGic * gic;
    bool end_on_eot;
    Tick int_delay;
};

#endif // __PARAMS__Pl011__
