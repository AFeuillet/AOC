import math
from utils import *

maxnb = 1000000
total = 0

for i in range(10, maxnb):
    digs = to_digit(i)
    subtotal = 0
    for d in digs:
        subtotal += math.factorial(int(d))
    if subtotal == i:
        total += i
        print("Curious number: %s" % (i))
print("Total: %s" % (total))
