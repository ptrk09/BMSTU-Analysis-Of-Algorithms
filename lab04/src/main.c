#include <stdio.h>

#include "threads.h"


#define INVALID_ARGS 2




uint64_t tick(void)
{
    uint32_t high, low;
    __asm__ __volatile__(
        "rdtsc\n"
        "movl %%edx, %0\n"
        "movl %%eax, %1\n"
        : "=r"(high), "=r"(low)::"%rax", "%rbx", "%rcx", "%rdx");

    uint64_t ticks = ((uint64_t)high << 32) | low;

    return ticks;
}


int main(int argc, char *argv[])
{
    setbuf(stdout, NULL);

    fprintf(stdout, "############ Параллельное умножение матриц ############\n");
    if (argc < 3)
    {
        return INVALID_ARGS;
    }

    args_t *args = create_args(N, M, K, atoi(argv[1]));
    if (!args)
    {
        return ALLOCATE_ERROR;
    }

    int type = atoi(argv[2]);
    if (3 == type)
    {

        uint64_t start = tick();
        base_m12n(args);
        uint64_t end = tick();

        fprintf(stdout, "Время исполнения: %lu (в тиках процессора)\n", end - start);
    }
    else
    {
        uint64_t start = tick();
        if (start_threading(args, atoi(argv[3]), type))
        {
            return ALLOCATE_ERROR;
        }
        uint64_t end = tick();

        fprintf(stdout, "Количество потоков: %s\nВремя исполнения: %lu (в тиках процессора)\n", argv[3], end - start);
    }

    return OK;
}
