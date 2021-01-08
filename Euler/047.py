from utils import *
from collections import Counter 


def prime_factors_bis(n):
	n = prime_factors(n)
	listb = list(set(n))
	for a in listb:
		listb.append(n.count(a) * a)
		listb.remove(a)
	return listb

maxfactor = 4
i = 1
while True:
	a = prime_factors_bis(i)
	b = prime_factors_bis(i + 1)
	c = prime_factors_bis(i + 2)
	d = prime_factors_bis(i + 3)

	if (len(a) == maxfactor and 
		len(b) == maxfactor and 
		len(c) == maxfactor and 
		len(d) == maxfactor and 
		len(set(a + b + c + d)) == maxfactor ** 2):
		print("Four consecutive, first: %s"% (i))
		exit()
	i += 1
