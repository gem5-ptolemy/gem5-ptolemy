#ifndef __PARAMS__InOrderTrace__
#define __PARAMS__InOrderTrace__

namespace Trace {
class InOrderTrace;
} // namespace Trace


#include "params/InstTracer.hh"

struct InOrderTraceParams
    : public InstTracerParams
{
    Trace::InOrderTrace * create();
};

#endif // __PARAMS__InOrderTrace__
