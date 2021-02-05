#ifndef __THREADS_H__
#define __THREADS_H__

#include <pthread.h>
#include <stdlib.h>

#include "m12n.h"
#include "struct.h"


#define OK 0
#define ALLOCATE_ERROR 1

int start_threading(args_t *args, const int cnt_threads, const int type);

#endif
