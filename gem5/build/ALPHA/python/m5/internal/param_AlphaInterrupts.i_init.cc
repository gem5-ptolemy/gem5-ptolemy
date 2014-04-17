#include "sim/init.hh"

extern "C" {
    void init_param_AlphaInterrupts();
}

EmbeddedSwig embed_swig_param_AlphaInterrupts(init_param_AlphaInterrupts);
