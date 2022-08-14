from utils import *
maxi = 50000000

primes = all_primes(int(sqrt(maxi)))
setnb = set()
for i in primes:
	pi = pow(i, 2)
	for j in primes:
		pj = pow(j, 3)
		if pj > maxi:
			break
		for k in primes:
			som =  pi + pj + pow(k, 4)
			if som < maxi:
				setnb.add(som)
			else:
				break
print(len(setnb))