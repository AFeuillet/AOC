nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

total = 0
for nb in nbl:
	chains = [[int(n) for n in nb.split(' ')]]
	cur = 0
	subtot = 0
	while(True):
		if chains[cur].count(0) == len(chains[cur]):
			break
		nwchain = []
		for i in range(len(chains[cur]) - 1):
			nwchain.append(chains[cur][i + 1] - chains[cur][i])
		subtot += chains[cur][len(chains[cur]) - 1]
		chains.append(nwchain)
		cur += 1
	total += subtot
print(total)