from utils import *


def is_lychrel(n):
	for l in range(50):
		pal = n + int(str(n)[::-1])
		if is_palindrome(pal):
			return False
		n = pal
	return True

total = 0
for i in range(10, 10000):
	if is_lychrel(i):
		total += 1
print("Number of Lychrel: %s" % (total))
