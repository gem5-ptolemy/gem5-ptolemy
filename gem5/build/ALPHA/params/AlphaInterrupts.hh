#ifndef __PARAMS__AlphaInterrupts__
#define __PARAMS__AlphaInterrupts__

namespace AlphaISA {
class Interrupts;
} // namespace AlphaISA


#include "params/SimObject.hh"

struct AlphaInterruptsParams
    : public SimObjectParams
{
    AlphaISA::Interrupts * create();
};

#endif // __PARAMS__AlphaInterrupts__
