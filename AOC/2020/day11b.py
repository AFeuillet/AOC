import copy
from os import system
from time import sleep


nfile = open('data/day11.txt', 'r')
nbl = nfile.read().split('\n')

nbl2= []
for line in nbl:
	nbl2.append(list(line))

def nbadjocc(i, j):
	nbad = 0
	jmax = len(nbl2[i])
	imax = len(nbl2)
	if i > 0 and j > 0:
		for k in range(1, imax):
			if i - k < 0 or j - k < 0:
				break
			c = nbl2[i - k][j - k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if i > 0:
		for k in range(i - 1, -1, -1):
			c = nbl2[k][j]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if i > 0 and j < jmax :
		for k in range(1, imax):
			if i - k < 0 or j + k >= len(nbl2[i - k]):
				break
			c = nbl2[i - k][j + k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if j > 0:
		for k in range(j - 1, -1, -1):
			c = nbl2[i][k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if j < jmax:
		for k in range(j + 1, len(nbl2[j])):
			c = nbl2[i][k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if i < imax and j > 0:
		for k in range(1, imax):
			if i + k >= imax or j - k < 0:
				break
			c = nbl2[i + k][j - k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if i < imax:
		for k in range(i + 1, imax):
			c = nbl2[k][j]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	if i < imax and j < jmax:
		for k in range(1, imax):
			if i + k >= imax or j + k >= len(nbl2[i + k]):
				break
			c = nbl2[i + k][j + k]
			if c == '#':
				nbad += 1
				break
			elif c == 'L':
				break
	return nbad

changed = True
while changed :
	changed = False
	nbl3 =[]
	for i in range(len(nbl2)):
		line2=[]
		for j in range(len(nbl2[i])):
			if nbl2[i][j] == '.':
				line2.append(nbl2[i][j])
				continue
			nb_adj = nbadjocc(i, j)
			if nbl2[i][j] == 'L' and nb_adj == 0:
				line2.append('#')
				changed = True
			elif nbl2[i][j] == '#' and nb_adj >= 5:
				line2.append('L')
				changed = True
			else:
				line2.append(nbl2[i][j])
		nbl3.append(line2)
	nbl2 = copy.deepcopy(nbl3)
occs = 0
for i in range(len(nbl2)):
	for j in range(len(nbl2[i])):
		if nbl2[i][j] == '#':
			occs +=1
print(occs)