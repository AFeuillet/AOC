nfile = open('data/day03.txt', 'r')
nbl = nfile.read().split('\n')

def getgen(pos, gen, ox):
	gcount = 0
	newone = []
	newzero = []
	for con in gen:
		if con[pos] == '1':
			gcount += 1
			newone.append(con)
		else:
			newzero.append(con)
	if gcount >= len(gen) / 2:
		return newone if ox==1 else newzero
	else:
		return newzero if ox==1 else newone

def getval(ox):
	i = 0
	nt = getgen(i, nbl, ox)
	while (len(nt) != 1):
		i += 1
		nt = getgen(i, nt, ox)
	return int(nt[0], 2)

print(getval(1) * getval(0))