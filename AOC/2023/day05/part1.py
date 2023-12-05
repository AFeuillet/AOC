nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

seeds = []
chains = []

seeds = [int(n) for n in nbl.pop(0).split(': ')[1].split(' ')]
nbl.pop(0)
mm = []
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