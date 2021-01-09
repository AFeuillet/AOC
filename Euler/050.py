from utils import *


maxprimes = 50000
primelist = []
for i in range(1, maxprimes):
	if is_prime(i):
		primelist.append(i)

maxfind = 1000000
maxsum = 0
maxit = 0
for i in range(len(primelist)):
	subsum = 0
	nbmaxit = 0
	for j in range(i, len(primelist)):
		subsum += primelist[j]
		if subsum < maxfind:
			nbmaxit += 1
			if subsum in primelist or is_prime(subsum):
				if nbmaxit > maxit:
					maxsum = subsum
					maxit = nbmaxit
		else:
			break
print("Max sum is: %s, nb iteration %s" % (maxsum, maxit))