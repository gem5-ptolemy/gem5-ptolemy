#ifndef __PARAMS__Tsunami__
#define __PARAMS__Tsunami__

class Tsunami;

#include <cstddef>
#include "params/System.hh"

#include "params/Platform.hh"

struct TsunamiParams
    : public PlatformParams
{
    Tsunami * create();
    System * system;
};

#endif // __PARAMS__Tsunami__
