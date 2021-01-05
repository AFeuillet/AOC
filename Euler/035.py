from utils import *

maxnb = 1000000
total = 0

def is_circ(n):
    digs = str(n)
    for d in range(1, len(digs)):
        if not is_prime(int(''.join(digs[d:]+digs[:d]))):
            return False
    return True

for i in range(maxnb):
    if is_prime(i):
        if i < 10 or is_circ(i):
			total += 1
			print("Circular number: %s" % (i))
print("Total: %s" % (total))