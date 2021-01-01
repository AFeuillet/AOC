maxcycle = 0
dmax = 0
for i in range(2, 1000):
	restes = []
	diviseurs = []
	reste = 10
	while reste != 0:
		diviseur = reste // i
		reste = reste % i
		if reste in restes:
			break
		restes.append(reste)
		diviseurs.append(diviseur)
		reste *= 10

	if reste != 0 and len(diviseurs) > maxcycle:
		dmax = i
		maxcycle = len(diviseurs)
print(dmax)