#include "sim/init.hh"

extern "C" {
    void init_param_Tru64AlphaSystem();
}

EmbeddedSwig embed_swig_param_Tru64AlphaSystem(init_param_Tru64AlphaSystem);
