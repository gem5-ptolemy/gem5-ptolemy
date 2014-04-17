#include "sim/init.hh"

extern "C" {
    void init_param_TsunamiPChip();
}

EmbeddedSwig embed_swig_param_TsunamiPChip(init_param_TsunamiPChip);
