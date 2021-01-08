from utils import *


for i in range(1000, 9999):
	for j in range(1, 8999):
		if i + j * 2 > 9999:
			continue
		if (sorted(str(i)) == sorted(str(i + j)) and 
			sorted(str(i)) == sorted(str(i + j * 2)) and 
			is_prime(i) and is_prime(i + j) and is_prime(i + j * 2)):
			print("Three prime permutations: %s%s%s + %s" % (i, i + j, i + j*2, j))