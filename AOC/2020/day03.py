nfile = open('data/day03.txt', 'r')
nbl = nfile.read().split('\n')

def move(right, bottom):
	col = 0
	lin = -1
	count = 0
	for line in nbl:
		lin += bottom
		if lin == 0:
			continue
		nex = col + right
		if nex > len(line) - 1:
			nex = nex - len(line)
		if(line[nex] == '#'):
			count +=1
		col = nex
	return count

print(move(3, 1))
