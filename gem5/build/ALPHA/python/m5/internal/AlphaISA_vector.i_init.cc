#include "sim/init.hh"

extern "C" {
    void init_AlphaISA_vector();
}

EmbeddedSwig embed_swig_AlphaISA_vector(init_AlphaISA_vector);
