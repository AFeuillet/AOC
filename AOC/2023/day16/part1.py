import sys

sys.setrecursionlimit(10000) 
nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

floors = []
for nb in nbl:
	floors.append(list(nb))
	print(nb)

nrjs = [['.' for j in fl] for fl in floors]

bim = {}
def getNext(prev, cur):
	if cur[1] >= len(floors) or cur[0] >= len(floors[0]) or cur[1] < 0 or cur[0] < 0:
		return False

	tile = floors[cur[1]][cur[0]]
	
	nrjs[cur[1]][cur[0]] = '#'

	pair = (cur[0], cur[1])
	if pair not in bim:
		bim[pair] = []
	if prev[0] == cur[0] - 1:
		if '>' in bim[pair]:
			return False
		else:
			bim[pair].append('>')
	elif prev[0] == cur[0] + 1:
		if '<' in bim[pair]:
			return False
		else:
			bim[pair].append('<')
	elif prev[1] == cur[1] - 1:
		if 'v' in bim[pair]:
			return False
		else:
			bim[pair].append('v')
	elif prev[1] == cur[1] + 1:
		if '^' in bim[pair]:
			return False
		else:
			bim[pair].append('^')

	if tile == '.':
		x = cur[0] + (cur[0] - prev[0])
		y = cur[1] + (cur[1] - prev[1])
		getNext(cur, [x, y])
	elif tile == '|':
		if prev[0] == cur[0] - 1 or prev[0] == cur[0] + 1:
			getNext(cur, [cur[0], cur[1] + 1])
			getNext(cur, [cur[0], cur[1] - 1])
		elif prev[1] == cur[1] - 1:
			getNext(cur, [cur[0], cur[1] + 1])
		else:
			getNext(cur, [cur[0], cur[1] - 1])
	elif tile == '-':
		if prev[1] == cur[1] - 1 or prev[1] == cur[1] + 1:
			getNext(cur, [cur[0] - 1, cur[1]])
			getNext(cur, [cur[0] + 1, cur[1]])
		elif prev[0] == cur[0] - 1:
			getNext(cur, [cur[0] + 1, cur[1]])
		else:
			getNext(cur, [cur[0] - 1, cur[1]])
	elif tile == '/':
		if prev[0] == cur[0] - 1:
			getNext(cur, [cur[0], cur[1] - 1])
		elif prev[1] == cur[1] - 1:
			getNext(cur, [cur[0] - 1, cur[1]])
		elif prev[0] == cur[0] + 1:
			getNext(cur, [cur[0], cur[1] + 1])
		else:
			getNext(cur, [cur[0] + 1, cur[1]])
	elif tile == '\\':
		if prev[0] == cur[0] - 1:
			getNext(cur, [cur[0], cur[1] + 1])
		elif prev[1] == cur[1] - 1:
			getNext(cur, [cur[0] + 1, cur[1]])
		elif prev[0] == cur[0] + 1:
			getNext(cur, [cur[0], cur[1] - 1])
		else:
			getNext(cur, [cur[0] - 1, cur[1]])


getNext([-1, 0], [0, 0])

for nrj in nrjs:
	print(nrj)
print(len(bim))
