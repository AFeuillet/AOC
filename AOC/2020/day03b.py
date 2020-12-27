nfile = open('data/day03.txt', 'r')
nbl = nfile.read().split('\n')

def move(right, bottom):
	col = 0
	count = 0
	for lin in range(bottom, len(nbl), bottom):
		nex = col + right
		line = nbl[lin]
		if nex > len(line) - 1:
			nex = nex - len(line)
		if(line[nex] == '#'):
			count +=1
		col = nex
	return count

a = move(1, 1)
b = move(3, 1)
c = move(5, 1)
d = move(7, 1)
e = move(1, 2)
print(a * b * c * d * e)