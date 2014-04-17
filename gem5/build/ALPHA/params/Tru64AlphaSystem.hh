#ifndef __PARAMS__Tru64AlphaSystem__
#define __PARAMS__Tru64AlphaSystem__

class Tru64AlphaSystem;


#include "params/AlphaSystem.hh"

struct Tru64AlphaSystemParams
    : public AlphaSystemParams
{
    Tru64AlphaSystem * create();
};

#endif // __PARAMS__Tru64AlphaSystem__
