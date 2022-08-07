from utils import *
import math

totm = 10 ** 7
minn = 0
minratio = 9999999


"""
# First method, brut force, too long :)
def totient_old(n):
	tot = 0
	for i in range(1, n + 1):
		if math.gcd(n, i) == 1:
			tot += 1
	return tot
"""

# second method using Euler formula https://en.wikipedia.org/wiki/Euler%27s_totient_function
def totient(n):
	primes = set(prime_factors(n))
	tot = n
	for prime in primes:
		tot *= 1 - (1 / prime)
	return int(tot)

for n in range(2, totm + 1):
	toti = totient(n)
	if (n / toti) < minratio and sorted(str(toti)) == sorted(str(n)):
			minratio = n / toti
			minn = n
print(minn)
