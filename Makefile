
uname_m = $(shell uname -m)
ARCH = $(uname_m)

CC=gcc
default: build
test.o: test.c
	echo 'from make:'
	gcc -c -Wall test.c 
build: test.o
	gcc -o test -Wall test.o
#	ld test.o -o test -lc --dynamic-linker /lib64/ld-2.17.so
clean:
	rm -f test.o
	rm -f test
info:

ifeq ($(ARCH),x86_64)
	echo "ok -$(ARCH)\n" 
else
	echo "not ok arch -$(ARCH)\n"	
endif

test: build
	chmod +x test
	./test
