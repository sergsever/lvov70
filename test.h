#ifndef __TEST_H
#define __TEST_H
typedef struct {
	unsigned int len;
	unsigned int chunknum : 24;
	unsigned int flags : 8;
} TFWStr;
#endif
