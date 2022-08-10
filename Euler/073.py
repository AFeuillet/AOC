import math

maxi = 12001
total = 0
for d in range(1, maxi):
	for n in range(1, d):
		if math.gcd(n, d) == 1 and n / d > 1 / 3 and n / d < 1 / 2:
			total += 1
print(total)
