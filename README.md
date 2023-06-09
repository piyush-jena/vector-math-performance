# High Performance Vector Math
This repository shows a non-GPU way to get faster linear algebra calculations.
We test some software and hardware optimizations to get speedup.

## Content
1. C simple
2. C unroll
3. C - Intel MKL
4. Python simple
5. Python numpy

## Running Instructions
1. Requires C, Intel MKL library, Python and numpy
2. For best performance for C programs compile with -O3 flag for compiler level optimizations 
```bash
gcc program.c -O3 -o program
```
3. To compile C program with Intel MKL
```bash
gcc program.c -O3 -lm -o program
```

## Dot Product Observations:
| Algorithm             | Vector Size | Runtime(sec) | Bandwidth (GB/s) |  Throughput   |
|-----------------------|-------------|--------------|------------------|---------------|
| C simple              | 1,000,000   | 0.001501 sec |  5.330960        | 1.333 GFLOPS  |
| C simple              | 300,000,000 | 0.457934 sec |  5.240930        | 1.310 GFLOPS  |
| C unroll              | 1,000,000   | 0.000465 sec |  17.202948       | 4.301 GFLOPS  |
| C unroll              | 300,000,000 | 0.208287 sec |  11.522536       | 2.881 GFLOPS  |
| C - Intel MKL         | 1,000,000   | 0.000194 sec |  41.342320       |10.336 GFLOPS  |
| C - Intel MKL         | 300,000,000 | 0.093496 sec |  25.669479       | 6.417 GFLOPS  |
| Python simple         | 1,000,000   | 0.610351 sec |  0.013107        |0.00328 GFLOPS |
| Python simple         | 300,000,000 | 177.1355 sec |  0.013549        |0.00339 GFLOPS |
| Python numpy          | 1,000,000   | 0.001509 sec |  5.301609        | 1.3254 GFLOPS |
| Python numpy          | 300,000,000 | 0.452451 sec |  5.304442        | 1.3261 GFLOPS |

## License
[MIT](https://choosealicense.com/licenses/mit/)
