#ifndef __PARAMS__FreebsdAlphaSystem__
#define __PARAMS__FreebsdAlphaSystem__

class FreebsdAlphaSystem;


#include "params/AlphaSystem.hh"

struct FreebsdAlphaSystemParams
    : public AlphaSystemParams
{
    FreebsdAlphaSystem * create();
};

#endif // __PARAMS__FreebsdAlphaSystem__
