#include "sim/init.hh"

extern "C" {
    void init_param_FreebsdAlphaSystem();
}

EmbeddedSwig embed_swig_param_FreebsdAlphaSystem(init_param_FreebsdAlphaSystem);
