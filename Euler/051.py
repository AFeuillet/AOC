from itertools import permutations
from utils import *


nbinco = 3
for i in range(999):
	stri = str(i) + 'X' * nbinco + '0' * (nbinco - len(str(i)))
	for perm in permutations(stri):
		nbperm = 0
		for j in range(10):
			isprim = int(''.join(perm).replace('X', str(j)))
			if isprim > 10000 and is_prime(isprim):
				nbperm += 1
		if nbperm == 8:
			print("8 permutations: %s " % (''.join(perm)))
			exit()