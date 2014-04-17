#ifndef __PARAMS__ArmISA__
#define __PARAMS__ArmISA__

namespace ArmISA {
class ISA;
} // namespace ArmISA

#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/SimObject.hh"

struct ArmISAParams
    : public SimObjectParams
{
    ArmISA::ISA * create();
    uint32_t fpsid;
    uint32_t id_mmfr0;
    uint32_t id_mmfr1;
    uint32_t id_mmfr2;
    uint32_t id_mmfr3;
    uint32_t id_pfr1;
    uint32_t id_pfr0;
    uint32_t id_isar1;
    uint32_t id_isar0;
    uint32_t id_isar3;
    uint32_t id_isar2;
    uint32_t id_isar5;
    uint32_t id_isar4;
    uint32_t midr;
};

#endif // __PARAMS__ArmISA__
