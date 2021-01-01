from utils import *


minrange = -1000
maxrange = 1000
maxprim = 0
for a in range(minrange, maxrange):
	for b in range(minrange, maxrange):
		prims = True
		n = 0
		while prims:
			prims = is_prime(n ** 2 + a * n + b)
			n += 1
		if n > maxprim:
			maxprim = n
			print("n:%s a:%s b:%s a*b:%s" % (n, a, b, a * b))
