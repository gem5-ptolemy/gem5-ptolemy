#ifndef __PARAMS__LinuxArmSystem__
#define __PARAMS__LinuxArmSystem__

class LinuxArmSystem;

#include <cstddef>
#include <cstddef>
#include <cstddef>
#include "enums/ArmMachineType.hh"
#include <cstddef>
#include <string>
#include <cstddef>
#include <cstddef>
#include <cstddef>
#include "base/types.hh"

#include "params/ArmSystem.hh"

#include "enums/ArmMachineType.hh"

struct LinuxArmSystemParams
    : public ArmSystemParams
{
    LinuxArmSystem * create();
    bool early_kernel_symbols;
    bool panic_on_oops;
    Enums::ArmMachineType machine_type;
    std::string dtb_filename;
    bool enable_context_switch_stats_dump;
    bool panic_on_panic;
    Addr atags_addr;
};

#endif // __PARAMS__LinuxArmSystem__
