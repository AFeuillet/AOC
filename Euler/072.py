from utils import *
import math

d = 1000000

"""
total = 0
# First method, brut force, too long :)
for i in range(1, d + 1):
	for j in range(i + 1, d + 1):
		if math.gcd(j, i) == 1:
			total += 1
print(total)
"""

# Second method using totien
# For 8
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# For 8 order on d
# 1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/6, 5/6, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1/8, 3/8, 5/8, 7/8
# totien(2), totien(3) .. totien(8)
total = 0
for i in range(2, d + 1):
	print(i)
	total += totient(i)
print(total)

#303963552391