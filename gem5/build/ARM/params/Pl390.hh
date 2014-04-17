#ifndef __PARAMS__Pl390__
#define __PARAMS__Pl390__

class Pl390;

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/BaseGic.hh"

struct Pl390Params
    : public BaseGicParams
{
    Pl390 * create();
    uint32_t it_lines;
    Addr dist_addr;
    Tick cpu_pio_delay;
    Tick dist_pio_delay;
    Addr cpu_addr;
    Tick int_latency;
    Addr msix_addr;
};

#endif // __PARAMS__Pl390__
