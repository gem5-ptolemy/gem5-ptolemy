#include "sim/init.hh"

extern "C" {
    void init_param_LinuxAlphaSystem();
}

EmbeddedSwig embed_swig_param_LinuxAlphaSystem(init_param_LinuxAlphaSystem);
