from utils import *


diag = 1
nbcount = 1
nbprim = 0
size = 0
while True:
	size += 2
	for i in range(4):
		diag += size
		if is_prime(diag):
			nbprim += 1
		nbcount += 1
	percent = nbprim * 100 / nbcount
	print("Total: %s number of prime: %s percent: %s, size:%s" % (nbcount, nbprim, percent, size + 1))
	if percent < 10:
		exit()