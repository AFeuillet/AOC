from utils import *


tri = 0
i = 1
while True:
    tri += i
    n = len(factors_optimized(tri))
    if n >= 500:
        print("triangle: %s nbdiv:%s" % (tri, n))
        exit()
    i += 1
