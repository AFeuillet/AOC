maxp = 99999
T = []
P = []
H = []
for n in range(0, maxp):
    T.append(int((n * (n + 1 ) / 2)))
    P.append(int((n * (3 * n - 1 ) / 2)))
    H.append(int((n * (2 * n - 1 ))))

for triangle in T:
	if triangle in P and triangle in H:
		if triangle > 40755:
			print("Pentagonal and hexagonal triangle: %s" % (triangle))
			exit()
