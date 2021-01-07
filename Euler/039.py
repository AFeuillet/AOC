maxp = 0
bigest = 0
sol = {}
for a in range(1, 999):
	for b in range(1, 999):
		for c in range(1, 999):
			if a ** 2 + b ** 2 == c ** 2 and a + b + c <= 1000:
				if a > b:
					stri = (b, a, c)
				else:
					stri = (a, b, c)
				if a + b + c not in sol:
					sol[a + b + c] = set()
				sol[a + b + c].add(stri)
				if maxp < len(sol[a + b + c]):
					maxp = len(sol[a + b + c])
					bigest = a + b + c
print('Perimiter: %s : %s' % (bigest, sol[bigest]))