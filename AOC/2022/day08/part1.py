nbl = open('data.txt').read().split('\n')

total = 0

forest = []
visibles = []

for iline, line  in enumerate(nbl):
	forest.append([])
	visibles.append([])
	for itree, tree in enumerate(line):
		forest[iline].append(int(tree))
		if iline == 0 or iline == len(nbl) - 1:
			visibles[iline].append(1)
		elif itree == 0 or itree == len(line) - 1:
			visibles[iline].append(1)
		else:
			visibles[iline].append(0)

for i in range(1, len(forest[0]) - 1):
	for j in range(1, len(forest[i]) - 1):
		tree = forest[i][j]
		if (max(forest[i][:j]) < tree or 
			max(forest[i][(j + 1):]) < tree or 
			max([forest[k][j] for k in range(0, i)]) < tree or 
			max([forest[k][j] for k in range(i + 1, len(forest[0]))]) < tree):
			visibles[i][j] = 1

for trees in visibles:
	total += trees.count(1)

print('Part 1: {}'.format(total))
