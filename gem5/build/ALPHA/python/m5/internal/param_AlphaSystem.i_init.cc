#include "sim/init.hh"

extern "C" {
    void init_param_AlphaSystem();
}

EmbeddedSwig embed_swig_param_AlphaSystem(init_param_AlphaSystem);
