nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

seeds = []
chains = []

seedi = [int(n) for n in nbl.pop(0).split(': ')[1].split(' ')]
seeds = []
for i in range(0, len(seedi), 2):
	for j in range(seedi[i], seedi[i] + seedi[i + 1], 1):
		seeds.append(j)

nbl.pop(0)
mm = []
print(seeds)
for nb in nbl:
	if nb and nb[0].isdigit():
		cc = nb.split(' ')
		mm.append([int(cc[1]), int(cc[1]) + int(cc[2]), int(cc[0])])
	elif nb == '':
		chains.append(mm)
		mm = []

def subchaines(idd, chain):
	for subc in chain:
		if idd >= subc[0] and idd < subc[1]:
			return(subc[2] + (idd - subc[0]))
	return idd

def parcours(idd):
	for chain in chains:
		idd = subchaines(idd, chain)
	return idd

minn = 999999999
for seed in seeds:
	minn = min(minn, parcours(seed))
print(minn)