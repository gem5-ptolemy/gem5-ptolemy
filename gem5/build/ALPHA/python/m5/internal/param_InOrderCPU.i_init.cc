#include "sim/init.hh"

extern "C" {
    void init_param_InOrderCPU();
}

EmbeddedSwig embed_swig_param_InOrderCPU(init_param_InOrderCPU);
