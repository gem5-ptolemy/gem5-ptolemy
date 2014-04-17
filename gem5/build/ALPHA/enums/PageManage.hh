#ifndef __ENUM__PageManage__
#define __ENUM__PageManage__

namespace Enums {
    enum PageManage {
        open = 0,
        open_adaptive = 1,
        close = 2,
        Num_PageManage = 3
    };
extern const char *PageManageStrings[Num_PageManage];
}

#endif // __ENUM__PageManage__
