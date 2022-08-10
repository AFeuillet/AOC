import math


# First method Brut, cannot solve all
def diop(i):
	maxi = 500
	for x in range(1, maxi):
		for y in range(1, maxi):
			if x ** 2 - i * y ** 2 == 1:
				return x
	return "NON TROUVE"

# Second method Pell's Equation
def pell(i):
	x = int(math.sqrt(i))
	y = x
	z = 1
	r = x << 1
	e1 = 1
	e2 = 0
	f1 = 0
	f2 = 1

	j = 0
	while True and 500000 > j:
		y = r * z - y
		z = (i - y ** 2) // z
		r = (x + y) // z

		e1, e2 = e2, e1 + e2 * r
		f1, f2 = f2, f1 + f2 * r

		a = f2 * x + e2
		b = f2
		if a ** 2 - i * b ** 2 == 1:
			return a
		j += 1
	return "NON TROUVE"

maxv = 0
dmax = 0
for i in range(1, 1001):
	if math.sqrt(i).is_integer():
		continue
	val = pell(i)
	if val > maxv:
		dmax = i
		maxv = val

print(dmax)