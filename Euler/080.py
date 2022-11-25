from decimal import *
import math
getcontext().prec = 150

# 3 methods
# First multiply to find to the most aaccurate
total = 0
for i in range(100):
	if math.sqrt(i).is_integer():
		continue
	r = math.isqrt(i)
	k = 0
	ti = '%s.' % r
	while k < 100:
		rac = ''
		oldies = 0
		for j in range(10):
			fi = Decimal(ti + str(j))
			if i > fi * fi:
				oldies = j
			else:
				ti += str(oldies)
				total += int(oldies)
				break
		if j == 9 and i > fi * fi:
			ti += '9'
			total += 9
		k += 1
	total -= oldies
	total += math.isqrt(i)
print(total)

# Easy sum
total = 0
for r in range(1, 100):
	if not math.sqrt(r).is_integer():
		total += sum(int(i) for i in str(Decimal(r).sqrt())[2:101])
		total += math.isqrt(r)
print(total)

# Soustraction computation
total = 0
for i in range(1, 100):
	if i in [1, 4, 9, 16, 25, 36, 49, 64, 81]:
		continue
	a = 5 * i
	b = 5
	interim = 0
	while len(str(b)) < 102:
		if a >= b:
			a -= b
			b += 10
		else:
			a *= 100
			strb = str(b)
			b = (b // 10) * 100 + 5
	for j in range(100):
		total += int(str(b)[j])
print(total)

