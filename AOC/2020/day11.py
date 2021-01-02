from os import system
from time import sleep

nfile = open('data/day11.txt', 'r')
nbl = nfile.read().split('\n')

nbl2= []
for line in nbl:
	nbl2.append(list(line))

def nbadjocc(i, j):
	nbad = 0
	if i > 0 and j > 0 and nbl2[i-1][j-1] == '#':
		nbad += 1
	if i > 0 and nbl2[i-1][j] == '#':	
		nbad += 1
	if i > 0 and j < len(nbl2[i]) - 1 and nbl2[i-1][j+1] == '#':	
		nbad += 1
	if j > 0 and nbl2[i][j-1] == '#':
		nbad += 1
	if j < len(nbl2[i]) - 1 and nbl2[i][j+1] == '#':
		nbad += 1
	if i < len(nbl2) - 1 and j > 0 and nbl2[i+1][j-1] == '#':
		nbad += 1
	if i < len(nbl2) - 1 and nbl2[i+1][j] == '#':
		nbad += 1
	if i < len(nbl2) - 1 and j < len(nbl2[i]) - 1 and nbl2[i+1][j+1] == '#':
		nbad += 1
	return nbad

system('clear')
changed = True
while changed:
	changed = False
	nbl3 =[]
	for i in range(len(nbl2)):
		line2=[]
		for j in range(len(nbl2[i])):
			if nbl2[i][j] == 'L' and nbadjocc(i, j) == 0:
				line2.append('#')
				changed = True
			elif nbl2[i][j] == '#' and nbadjocc(i, j) >= 4:
				line2.append('L')
				changed = True
			else:
				line2.append(nbl2[i][j])
		nbl3.append(line2)
		print(''.join(line2))
	nbl2 = nbl3
	sleep(0.2)
	system('clear')

occs = 0
for i in range(len(nbl2)):
	for j in range(len(nbl2[i])):
		if nbl2[i][j] == '#':
			occs +=1
print(occs)