#ifndef __PARAMS__AlphaISA__
#define __PARAMS__AlphaISA__

namespace AlphaISA {
class ISA;
} // namespace AlphaISA


#include "params/SimObject.hh"

struct AlphaISAParams
    : public SimObjectParams
{
    AlphaISA::ISA * create();
};

#endif // __PARAMS__AlphaISA__
