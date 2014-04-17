#include "sim/init.hh"

extern "C" {
    void init_param_TsunamiIO();
}

EmbeddedSwig embed_swig_param_TsunamiIO(init_param_TsunamiIO);
