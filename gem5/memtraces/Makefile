default: all

GEM5 = ../build/ARM/gem5.opt
GEM5_OPTS = --outdir=
DEBUG_FLAGS = --debug-flags=Bus,MemoryAccess
PY_SCRIPT = ../configs/example/se.py
PY_OPTS = --caches --l1d_size=4kB --l1i_size=4kB
WCET_DIR = $(abspath ../../wcet_bench)
CHStone_DIR = $(abspath ../../CHStone_v1.8_130128)

include $(CHStone_DIR)/Makefrag

WCET_OBJS = $(wildcard $(WCET_DIR)/*.o)
CHStone_OBJS = $(wildcard $(CHStone_DIR)/*/*.o)

WCET_MEMS = $(notdir $(patsubst %.o,%.mem,$(WCET_OBJS)))
CHStone_MEMS = $(notdir $(patsubst %.o,%.mem,$(CHStone_OBJS)))

wcet_object_copy: 
	cp $(WCET_OBJS) .
chstone_object_copy: 
	cp $(CHStone_OBJS) .

wcet: wcet_object_copy $(WCET_MEMS)
chstone: chstone_object_copy $(CHStone_MEMS)
%.mem: %.o
	$(GEM5) $(GEM5_OPTS)$@.out $(DEBUG_FLAGS) $(PY_SCRIPT) $(PY_OPTS) -c $< > $@

all: wcet chstone

clean:
	rm *.o *.mem
	rm -rf *.out
    
