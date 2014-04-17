#include "sim/init.hh"

extern "C" {
    void init_enum_ThreadModel();
}

EmbeddedSwig embed_swig_enum_ThreadModel(init_enum_ThreadModel);
