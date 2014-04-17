#ifndef __PARAMS__SrcClockDomain__
#define __PARAMS__SrcClockDomain__

class SrcClockDomain;

#include <cstddef>
#include "params/VoltageDomain.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/ClockDomain.hh"

struct SrcClockDomainParams
    : public ClockDomainParams
{
    SrcClockDomain * create();
    VoltageDomain * voltage_domain;
    Tick clock;
};

#endif // __PARAMS__SrcClockDomain__
