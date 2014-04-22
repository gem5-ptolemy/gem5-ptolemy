OBJ = main.o fftmisc.o  fourierf.o
FILE = main.c fftmisc.c  fourierf.c
CFLAGS = -static -O3 -g

fft: ${OBJ} Makefile
	arm-linux-gnueabi-gcc  ${CFLAGS} ${OBJ} -o fft -lm
fftmisc.o: fftmisc.c
	arm-linux-gnueabi-gcc ${CFLAGS} -c fftmisc.c
fourierf.o: fourierf.c
	arm-linux-gnueabi-gcc ${CFLAGS} -c fourierf.c
main.o: main.c
	arm-linux-gnueabi-gcc ${CFLAGS} -c main.c

clean:
	rm -rf *.o fft output*
