#include "sim/init.hh"

extern "C" {
    void init_param_TsunamiCChip();
}

EmbeddedSwig embed_swig_param_TsunamiCChip(init_param_TsunamiCChip);
