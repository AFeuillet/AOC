from utils import *


def is_contiprime(n):
	for j in range(len(n), 0, -1):
		if not is_prime(int(n[-j:])) or not is_prime(int(n[:j])):
			return False
	return True

total = 0
nbfind = 0
i = 10
while nbfind < 11:
	if is_contiprime(str(i)):
		print("Continuous prime: %s" % (i))
		total += i
		nbfind += 1
	i += 1
print("Total: %s" % (total))