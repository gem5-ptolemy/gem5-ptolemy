#ifndef __PARAMS__LinuxAlphaSystem__
#define __PARAMS__LinuxAlphaSystem__

class LinuxAlphaSystem;

#include <cstddef>
#include "base/types.hh"

#include "params/AlphaSystem.hh"

struct LinuxAlphaSystemParams
    : public AlphaSystemParams
{
    LinuxAlphaSystem * create();
    Tick boot_cpu_frequency;
};

#endif // __PARAMS__LinuxAlphaSystem__
