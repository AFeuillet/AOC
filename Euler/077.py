from utils import *

maxprime = 1000
primes = []

for i in range(maxprime):
	if is_prime(i):
		primes.append(i)

target = 2
while True:
	ways = [0] * (target + 1) 
	ways[0] = 1

	for i in primes:
		for j in range(i, target + 1):
			ways[j] += ways[j - i]
			if ways[j] > 5000:
				print(j)
				exit()
	target += 1