#include "sim/init.hh"

extern "C" {
    void init_param_AlphaBackdoor();
}

EmbeddedSwig embed_swig_param_AlphaBackdoor(init_param_AlphaBackdoor);
