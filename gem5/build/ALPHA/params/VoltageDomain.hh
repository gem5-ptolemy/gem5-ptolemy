#ifndef __PARAMS__VoltageDomain__
#define __PARAMS__VoltageDomain__

class VoltageDomain;

#include <cstddef>

#include "params/SimObject.hh"

struct VoltageDomainParams
    : public SimObjectParams
{
    VoltageDomain * create();
    double voltage;
};

#endif // __PARAMS__VoltageDomain__
