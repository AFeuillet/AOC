nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

fields = []
loopi = []
startp = (0, 0)
larg, haut = 0, 0

def addIf(i, j):
	if (i, j) not in loopi:
		fields[i][j] = 'I'
		return True
	return False
 
# 123
# 4X5
# 678 
def addI(pos, i, j):
	if pos == 1:
		for h in range(i - 1, -1, -1):
			for l in range(j - 1, -1, -1):	
				if not addIf(h, l): 
					return 
	elif pos == 2:
		for h in range(i - 1, -1, -1):
			if not addIf(h, j): 
				return 
	elif pos == 3:
		for h in range(i - 1, -1, -1):
			for l in range(j + 1, larg):
				if not addIf(h, l): 
					return 
	elif pos == 4:
		for l in range(j - 1, -1, -1):
			if not addIf(i, l): 
				return
	elif pos == 5:
		for l in range(j + 1, larg):
			if not addIf(i, l): 
				return
	elif pos == 6:
		for h in range(i + 1, haut):
			for l in range(j - 1, -1, -1):
				if not addIf(i, l): 
					return
	elif pos == 7:
		for h in range(i + 1, haut):
			if not addIf(h, j): 
				return 
	elif pos == 8:
		for h in range(i + 1, haut):
			for l in range(j + 1, larg):
				if not addIf(h, l): 
					return 
	return

def setLoopi():
	last = loopi[len(loopi) - 2]
	cur = loopi[len(loopi) - 1]
	i, j = cur[0], cur[1]
	elt = fields[i][j]

	nwone = (0, 0)
	if elt == '-':
		nwone = (i, j + 1) if (i, j - 1) == last else (i, j - 1)
	elif elt == '|':
		nwone = (i + 1, j) if (i - 1, j) == last else (i - 1, j)
	elif elt == 'L':
		nwone = (i, j + 1) if (i - 1, j) == last else (i - 1, j)
	elif elt == 'J':
		nwone = (i, j - 1) if (i - 1, j) == last else (i - 1, j)
	elif elt == '7':
		nwone = (i + 1, j) if (i, j - 1) == last else (i, j - 1)
	elif elt == 'F':
		nwone = (i + 1, j) if (i, j + 1) == last else (i, j + 1)
	
	loopi.append(nwone)
	return nwone

def setAllI(pos):
	last = loopi[pos - 2]
	cur = loopi[pos - 1]
	i, j = cur[0], cur[1]
	elt = fields[i][j]
	if elt == '-':
		if (i, j - 1) == last:
			addI(2, i, j)
		else:
			addI(7, i, j)
	elif elt == '|':
		if (i - 1, j) == last:
			addI(5, i, j)
		else: 
			addI(4, i, j)
	elif elt == 'L':
		if (i - 1, j) == last:
			addI(3, i, j)
		else: 
			addI(4, i, j)
			addI(6, i, j)
			addI(7, i, j)
	elif elt == 'J':
		if (i - 1, j) == last:
			addI(5, i, j)
			addI(8, i, j)
			addI(7, i, j)
		else:
			addI(1, i, j)
	elif elt == '7':
		if (i, j - 1) == last:
			addI(2, i, j)
			addI(3, i, j)
			addI(5, i, j)
		else:
			addI(6, i, j)
	elif elt == 'F':
		if (i, j + 1) == last:
			addI(8, i, j)
		else:
			addI(4, i, j)
			addI(1, i, j)
			addI(2, i, j)
	return

startp = []
for i, nb in enumerate(nbl):
	if 'S' in nb:
		startp = (i, nb.index('S'))
		loopi.append(startp)
	fields.append(list(nb))

i = startp[0] 
j = startp[1]
larg, haut = len(fields[0]), len(fields)
starting = []
if i + 1 < haut and fields[i + 1][j] in ('|', 'J', 'L'):
	starting.append((i + 1, j))
if i - 1 > 0 and fields[i - 1][j] in ('|', 'F', '7'):
	starting.append((i - 1, j))
if j - 1 > 0 and fields[i][j - 1] in ('-', 'F', 'L'):
	starting.append((i, j - 1))
if j + 1 < larg and fields[i][j + 1] in ('-', 'J', '7'):
	starting.append((i, j + 1))

# Start direction 0 or 1
loopi.append(starting[0])
 
while setLoopi() != startp:
	continue

for i in range(2, len(loopi)):
	setAllI(i)

total = 0
for f in fields:
	total += f.count('I')
print(total)


"""
Tests sets

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........

..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........

..F-7
.FJ.|
FJ.FJ
S.FJ.
L7|..
.LJ..

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L

"""
