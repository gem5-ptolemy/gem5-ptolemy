default: all

SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)
DUMPS = $(SRCS:.c=.dump)

CC = arm-linux-gnueabi-gcc
C_OPTS = -static
DUMP_LINUX = arm-linux-gnueabi-objdump
DUMP_NON_LINUX = arm-none-eabi-objdump
DUMP_OPTS = -s

all: $(OBJS)
%.o: %.c
	$(CC) $(C_OPTS) -o $@ $<
dump: $(DUMPS)
%.dump: %.o
	$(DUMP_LINUX) $(DUMP_OPTS) $< > $@
clean:
	rm *.o *.dump
