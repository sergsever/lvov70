#ifndef __TEST_H
#define __TEST_H
#define flag1 = 1
#define flag2 = 2
#define flag3 = 3
#define flag4 = 4

typedef struct {
	unsigned int len;
	unsigned int chunknum : 24;
	unsigned int flags : 8;
} TFWStr;
#endif
