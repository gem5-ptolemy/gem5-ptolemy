#include "enums/ThreadModel.hh"
namespace Enums {
    const char *ThreadModelStrings[Num_ThreadModel] =
    {
        "Single",
        "SMT",
        "SwitchOnCacheMiss",
    };
} // namespace Enums
