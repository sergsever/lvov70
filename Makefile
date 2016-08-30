
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
y.tab.c: parser/http.y
	yacc -d parser/http.y
lex.yy.c: parser/http.l
	lex -l parser/http.l
lex.yy.o: lex.yy.c y.tab.h
	gcc -c lex.yy.c
y.tab.o: y.tab.c y.tab.h
	gcc -c y.tab.c
http: lex.yy.o y.tab.o
	gcc lex.yy.o y.tab.o -o http
clean:
	rm -f test.o
	rm -f test
	rm http y.tab.o lex.yy.o
	rm y.tab.c lex.yy.c
info:

ifeq ($(ARCH),x86_64)
	echo "ok -$(ARCH)\n" 
else
	echo "not ok arch -$(ARCH)\n"	
endif

test: build
	chmod +x test
	./test
