nfile = open('data/day15.txt', 'r')
nbl = nfile.read().split(',')
nbl = list(map(int, nbl))

lpos = dict()
i = 0
for inn in nbl:
	lpos[int(inn)] = i
	i += 1
while len(nbl) != 30000000:
	last = nbl[len(nbl)-1]
	if last in lpos:
		nex = len(nbl) -1 - lpos[last] 
	else:
		nex =0
	lpos[last] = len(nbl) -1
	nbl.append(nex)

print(nbl[len(nbl)-1])