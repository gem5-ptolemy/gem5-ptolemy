#include "sim/init.hh"

extern "C" {
    void init_param_SimpleDRAM();
}

EmbeddedSwig embed_swig_param_SimpleDRAM(init_param_SimpleDRAM);
