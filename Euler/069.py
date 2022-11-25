from utils import *

maxi = 1000000
valmax = 0
findi = 0
for n in range(2, maxi):
	tot = totient(n)
	val = n / tot
	if val > valmax:
		findi = n
		valmax = val

print(findi, valmax)
