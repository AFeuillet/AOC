from itertools import permutations
from utils import *


maxp = 0
maxperm = '123456789_'
for i in range(1, len(maxperm)):
	perms = permutations(maxperm[:-i], len(maxperm) - i)
	for j in perms:
		intj = int(''.join(j))
		if is_prime(intj):
			maxp = max(maxp, intj)
	if maxp != 0:
		print("Max Pandigital prime", maxp)
		exit()
