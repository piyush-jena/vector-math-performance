import numpy as np
import time
import sys

def dp(N,A,B):
    R = 0.0;
    for j in range(0,N):
        R += A[j]*B[j]
    return R

if len(sys.argv) != 3 :
    print("Usage: python3 dp4 x y")
    print("where x and y are integers.")
    print("x: size of the vector.")
    print("y: number of measurements.")
    exit()

size = sys.argv[1]
measurements = sys.argv[2]

total = 0.0

A = np.ones(int(size),dtype=np.float32)
B = np.ones(int(size),dtype=np.float32)

for i in range(0, int(measurements)):
    start = time.monotonic_ns()
    x = dp(int(size),A,B)
    end = time.monotonic_ns()

    if i >= (int(measurements)/2) :
        total = total + (end-start)/1000

average = total * 2 / int(measurements)

print("R = " + str(x))

print('N : ' + size + ' <T> : ' + str(round(average/1000000, 6)) + ' sec B : ' + str(round((float(size)*8.0)/(1000*average), 6)) + ' GB/sec F : ' + str(round((float(size)*2.0)/(1000*average), 6)) + ' GFLOP/sec');

# Xeon 16GB RAM N : 1000000 <T> : 0.610351 sec B : 0.013107 GB/sec F : 0.003277 GFLOP/sec
# Xeon 16GB RAM N : 300000000 <T> : 177.135515 sec B : 0.013549 GB/sec F : 0.003387 GFLOP/sec
