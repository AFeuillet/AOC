from utils import *


def is_goldbach(n):
	for a in range(n - 2, 0, -2):
		if is_prime(a):
			for c in range(1, n):
				if n == a + 2 * c ** 2:
					return True
	return False

i = 3
while True:
	if not is_prime(i): 
		if not is_goldbach(i):
			print("Found the first non Goldbach: %s" % (i))
			exit()
	i += 2