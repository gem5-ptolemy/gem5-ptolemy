#include "sim/init.hh"

extern "C" {
    void init_param_Tsunami();
}

EmbeddedSwig embed_swig_param_Tsunami(init_param_Tsunami);
