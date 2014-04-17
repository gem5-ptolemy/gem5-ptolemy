#ifndef __PARAMS__AlphaTLB__
#define __PARAMS__AlphaTLB__

namespace AlphaISA {
class TLB;
} // namespace AlphaISA

#include <cstddef>
#include "base/types.hh"

#include "params/BaseTLB.hh"

struct AlphaTLBParams
    : public BaseTLBParams
{
    AlphaISA::TLB * create();
    int size;
};

#endif // __PARAMS__AlphaTLB__
