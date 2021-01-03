nfile = open('data/day15.txt', 'r')
nbl = nfile.read().split(',')
nbl = list(map(int, nbl))

while len(nbl) != 2020:
	last = nbl[len(nbl)-1]
	nex = 0
	for i in range(len(nbl)-2, -1, -1):
		if last == nbl[i]:
			nex = len(nbl)-1 - i
			break
	nbl.append(nex)
print(nbl[len(nbl)-1])
