import math

maxi = 1500000

# Generating Pythagorean_triple
nb_p = 0
arr_p = [0] * (maxi + 1)
nmax = int(math.sqrt(maxi))

for m in range(2, nmax):
	for n in range(1, m + 1):
		if (n + m) % 2 == 1 and math.gcd(n, m) == 1:		
			a = (m ** 2 - n ** 2)
			b = (2 * m * n)
			c = (m ** 2 + n ** 2)
			d = a + b + c
			k = 1
			while k * d <= maxi:
				arr_p[k * d] += 1
				k += 1

print(arr_p.count(1))
