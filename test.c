/*test*/
#include "stdlib.h"
#include "test.h"


#include <linux/types.h>
#include "stdio.h"
# define lockdep_init_map(lock, name, key, sub) \
		do { (void)(name); (void)(key); } while (0)

#define lockdep(key, name) \
do { (void)(name); (void)(key); } while (0)
void printdata(void)
{
__u32 sam;



sam = 50;
}
printf("main funk:%d\n", sam);
}
int main(int argc, char **argv)
{

printdata();
return 0;
}
