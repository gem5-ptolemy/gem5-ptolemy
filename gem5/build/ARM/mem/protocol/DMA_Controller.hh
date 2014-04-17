/** \file DMA_Controller.hh
 *
 * Auto generated C++ code started by /Users/hokeunkim/Development/EE219D/gem5/src/mem/slicc/symbols/StateMachine.py:233
 * Created by slicc definition of Module "DMA Controller"
 */

#ifndef __DMA_CONTROLLER_HH__
#define __DMA_CONTROLLER_HH__

#include <iostream>
#include <sstream>
#include <string>

#include "mem/protocol/TransitionResult.hh"
#include "mem/protocol/Types.hh"
#include "mem/ruby/common/Consumer.hh"
#include "mem/ruby/common/Global.hh"
#include "mem/ruby/slicc_interface/AbstractController.hh"
#include "params/DMA_Controller.hh"
#include "mem/protocol/MessageBuffer.hh"
#include "mem/protocol/DMA_State.hh"
extern std::stringstream DMA_transitionComment;

class DMA_Controller : public AbstractController
{
  public:
    typedef DMA_ControllerParams Params;
    DMA_Controller(const Params *p);
    static int getNumControllers();
    void init();
    MessageBuffer* getMandatoryQueue() const;
    const std::string toString() const;

    void print(std::ostream& out) const;
    void wakeup();
    void clearStats();
    void regStats();
    void collateStats();

    void recordCacheTrace(int cntrl, CacheRecorder* tr);
    Sequencer* getSequencer() const;

    bool functionalReadBuffers(PacketPtr&);
    uint32_t functionalWriteBuffers(PacketPtr&);

    void countTransition(DMA_State state, DMA_Event event);
    void possibleTransition(DMA_State state, DMA_Event event);
    uint64 getEventCount(DMA_Event event);
    bool isPossible(DMA_State state, DMA_Event event);
    uint64 getTransitionCount(DMA_State state, DMA_Event event);

private:
    DMASequencer* m_dma_sequencer_ptr;
    Cycles m_request_latency;
    TransitionResult doTransition(DMA_Event event,
                                  const Address& addr);

    TransitionResult doTransitionWorker(DMA_Event event,
                                        DMA_State state,
                                        DMA_State& next_state,
                                        const Address& addr);

    int m_counters[DMA_State_NUM][DMA_Event_NUM];
    int m_event_counters[DMA_Event_NUM];
    bool m_possible[DMA_State_NUM][DMA_Event_NUM];

    static std::vector<Stats::Vector *> eventVec;
    static std::vector<std::vector<Stats::Vector *> > transVec;
    static int m_num_controllers;

    // Internal functions
    DMA_State getState(const Address& param_addr);
    void setState(const Address& param_addr, const DMA_State& param_state);
    AccessPermission getAccessPermission(const Address& param_addr);
    void setAccessPermission(const Address& param_addr, const DMA_State& param_state);
    DataBlock& getDataBlock(const Address& param_addr);

    // Actions
    /** \brief Send a DMA read request to memory */
    void s_sendReadRequest(const Address& addr);
    /** \brief Send a DMA write request to memory */
    void s_sendWriteRequest(const Address& addr);
    /** \brief Notify dma controller that write request completed */
    void a_ackCallback(const Address& addr);
    /** \brief Write data to dma sequencer */
    void d_dataCallback(const Address& addr);
    /** \brief Pop request queue */
    void p_popRequestQueue(const Address& addr);
    /** \brief Pop request queue */
    void p_popResponseQueue(const Address& addr);

    // Objects
    MessageBuffer* m_DMA_responseFromDir_ptr;
    MessageBuffer* m_DMA_reqToDirectory_ptr;
    MessageBuffer* m_DMA_mandatoryQueue_ptr;
    DMA_State* m_DMA_cur_state_ptr;
};
#endif // __DMA_CONTROLLER_H__
