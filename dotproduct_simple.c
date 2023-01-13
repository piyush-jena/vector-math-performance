#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float dp(long N, float *pA, float *pB) {
    float R = 0.0;
    int j;
    for (j=0;j<N;j++)
        R += pA[j]*pB[j];
    return R;
}

int main(int argc, char *argv[]) 
{
    int size, measurements;
    struct timespec start, end;
    double total = 0.0;
    double average = 0.0;

    if (argc != 3)
    {
        printf("Usage: ./dp1 x y \n");
        printf("where x and y are integers. \n");
        printf("x: size of the vector. \n");
        printf("y: number of measurements. \n");

        return -1;
    }
    
    sscanf(argv[1], "%d", &size);
    sscanf(argv[2], "%d", &measurements);

    float* pA = (float*)malloc((size)*sizeof(float));
    float* pB = (float*)malloc((size)*sizeof(float));

    for (int i = 0 ; i < size; i++)
        pA[i] = pB[i] = 1.0;
    
    for (int i = 0 ; i < measurements ; i++)
    {
        clock_gettime(CLOCK_MONOTONIC, &start);
        float x = dp(size, pA, pB);
        clock_gettime(CLOCK_MONOTONIC, &end);

        printf("R: %f \n", x); // Not printing or using x would allow compiler optimization to take over and skip the running of the function due to -O3 flag.
        double time_usec=(((double)end.tv_sec *1000000 + (double)end.tv_nsec/1000) - ((double)start.tv_sec *1000000 + (double)start.tv_nsec/1000));
        
        if (i >= (measurements/2))
            total += (double)time_usec;
    }

    average = total * 2 / ((double) measurements);
    
    printf("N : %d ", size);
    printf("<T> : %.6lf sec ", average/1000000);
    printf("B : %.6lf GB/sec ", (8.0 * (double)size) / (1000 * average));
    printf("F : %.3lf GFLOP/sec \n", (2.0 * (double)size) / (1000 * average));

    return 0;
}

// Xeon 16GB RAM N : 1000000 <T> : 0.001501 sec B : 5.330960 GB/sec F : = 1.333 GFLOP/sec (AC)
// Xeon 16GB RAM N : 300000000 <T> : 0.457934 sec B : 5.240930 GB/sec F : = 1.310 GFLOP/sec (WA)
