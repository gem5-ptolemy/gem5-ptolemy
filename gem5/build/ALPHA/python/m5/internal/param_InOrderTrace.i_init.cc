#include "sim/init.hh"

extern "C" {
    void init_param_InOrderTrace();
}

EmbeddedSwig embed_swig_param_InOrderTrace(init_param_InOrderTrace);
