/*test*/
#include "stdlib.h"
//#include "str.h"
#include "test.h"


#include <linux/types.h>
#include "stdio.h"

typedef struct TfwStr{
	struct sk_buff	*skb;
	unsigned long	len;
	unsigned char	eolen;

	unsigned int	chunknum : 24;
	unsigned int	flags : 8;
	union {
	char *data;
	struct TfwStr *chunks;
};
} TfwStr;
void printdata(void)
{
	 TfwStr s= {.data = "test", .len = 4};
	TfwStr ds = {.chunks = &s, .len = 4};

	printf("tfwstr:%s\n", ds.chunks->data);
}
int main(int argc, char **argv)
{

	printdata();
	return 0;
}
