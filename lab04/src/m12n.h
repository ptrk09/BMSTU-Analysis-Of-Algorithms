#ifndef __M12N_H__
#define __M12N_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "struct.h"



#define N 1024
#define M N
#define K N


void print_matrix(int **matrix);

void read_matrix(int **matrix, FILE *file);

void init_matrix(int **matrix);

int **create_matrix(int n, int m);

args_t *create_args(int n, int m, int k, int read_file);

void base_m12n(args_t *args);

void *parallel_m12n_1(void *args);

void *parallel_m12n_2(void *args);

#endif
