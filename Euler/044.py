maxp = 5000
p = [0]
for n in range(1, maxp):
    p.append(int((n * (3 * n - 1)) / 2))

for j in range(1, int(maxp / 2)):
	for k in range(j + 1, int(maxp / 2)):
		if (p[j] + p[k]) in p and abs(p[k] - p[j]) in p:
			print("Pentagonal Pair : %s, %s diff: %s" % (p[j], p[k], abs(p[k] - p[j])))
			exit()
		