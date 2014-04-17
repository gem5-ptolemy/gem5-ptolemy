#include "sim/init.hh"

extern "C" {
    void init_param_AlphaTLB();
}

EmbeddedSwig embed_swig_param_AlphaTLB(init_param_AlphaTLB);
