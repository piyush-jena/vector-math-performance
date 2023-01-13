import numpy as np
import time
import sys

if len(sys.argv) != 3 :
    print("Usage: python3 dp5 x y")
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
    x = np.dot(A,B)
    end = time.monotonic_ns()

    if i >= (int(measurements)/2) :
        total = total + (end-start)/1000

average = total * 2 / int(measurements)

print("R = " + str(x))

print('N : ' + size + ' <T> : ' + str(round(average/1000000, 6)) + ' sec B : ' + str(round((float(size)*8.0)/(1000*average), 6)) + ' GB/sec F : ' + str(round((float(size)*2.0)/(1000*average), 6)) + ' GFLOP/sec');

# Xeon 16GB RAM N : 1000000 <T> : 0.001509 sec B : 5.301609 GB/sec F : 1.325402 GFLOP/sec
# Xeon 16GB RAM N : 300000000 <T> : 0.452451 sec B : 5.304442 GB/sec F : 1.32611 GFLOP/sec
