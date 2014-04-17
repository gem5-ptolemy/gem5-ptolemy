#include "sim/init.hh"

extern "C" {
    void init_param_AlphaISA();
}

EmbeddedSwig embed_swig_param_AlphaISA(init_param_AlphaISA);
