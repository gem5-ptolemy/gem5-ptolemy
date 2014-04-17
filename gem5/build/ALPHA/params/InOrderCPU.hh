#ifndef __PARAMS__InOrderCPU__
#define __PARAMS__InOrderCPU__

class InOrderCPU;

#include <cstddef>
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "params/BranchPredictor.hh"
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
#include "enums/ThreadModel.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"
#include <cstddef>
#include "base/types.hh"

#include "params/BaseCPU.hh"

#include "enums/ThreadModel.hh"

struct InOrderCPUParams
    : public BaseCPUParams
{
    InOrderCPU * create();
    bool stageTracing;
    Cycles div16RepeatRate;
    Cycles div8RepeatRate;
    unsigned memBlockSize;
    Cycles div8Latency;
    BPredUnit * branchPred;
    unsigned cachePorts;
    Cycles div32RepeatRate;
    Cycles multRepeatRate;
    Cycles div32Latency;
    Cycles div16Latency;
    unsigned stageWidth;
    unsigned fetchBuffSize;
    Cycles div24Latency;
    Enums::ThreadModel threadModel;
    unsigned activity;
    Cycles multLatency;
    Cycles div24RepeatRate;
};

#endif // __PARAMS__InOrderCPU__
