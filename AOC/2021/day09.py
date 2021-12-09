nfile = open('data/day09.txt', 'r')
nbl = nfile.read().split('\n')

heightmap = []
for line in nbl:
	heightmap.append([int(a) for a in line])

def drawIt(paintin):
	for i in range(len(heightmap)):
		for j in range(len(heightmap[i])):
			print(paintin[i][j],  end ='')
		print()
	print()

def isLavaTube(i, j):
	return (
		(i + 1 >= len(heightmap) or heightmap[i][j] < heightmap[i + 1][j]) and 
		(i - 1 < 0 or heightmap[i][j] < heightmap[i - 1][j]) and 
		(j + 1 >= len(heightmap[i]) or heightmap[i][j] < heightmap[i][j + 1]) and 
		(j - 1 < 0 or heightmap[i][j] < heightmap[i][j - 1])
		)

total = 0 
for i in range(len(heightmap)):
	for j in range(len(heightmap[i])):
		if isLavaTube(i, j):
			total += heightmap[i][j] + 1
print("Part One: %s" % total)


def paint(paintin, i, j):
	if i + 1 < len(heightmap) and paintin[i + 1][j] == 0 and heightmap[i][j] < heightmap[i + 1][j] and heightmap[i + 1][j] < 9:
		paintin[i + 1][j] = ' '
		paint(paintin, i + 1, j)
	if i - 1 >= 0 and paintin[i - 1][j] == 0 and heightmap[i][j] < heightmap[i - 1][j] and heightmap[i - 1][j] < 9:
		paintin[i - 1][j] = ' '
		paint(paintin, i - 1, j)
	if j + 1 < len(heightmap[i]) and paintin[i][j + 1] == 0 and heightmap[i][j] < heightmap[i][j + 1] and heightmap[i][j + 1] < 9:
		paintin[i][j + 1] = ' '
		paint(paintin, i, j + 1)
	if j - 1 >= 0 and paintin[i][j - 1] == 0 and heightmap[i][j] < heightmap[i][j - 1] and heightmap[i][j - 1] < 9:
		paintin[i][j - 1] = ' '
		paint(paintin, i, j - 1)

bassins = []
for i in range(len(heightmap)):
	for j in range(len(heightmap[i])):
		if isLavaTube(i, j):
			paintin = [[0 for x in range(len(heightmap[0]))] for y in range(len(heightmap))]
			paintin[i][j] = 'X'
			paint(paintin, i, j)
			bassinSize = 0
			for a in range(len(heightmap)):
				for b in range(len(heightmap[i])): 
					if paintin[a][b] != 0:
						bassinSize += 1
			#drawIt(paintin)
			bassins.append(bassinSize)

x, y, z = sorted(bassins)[-3:]
print("Part Two: %s" % (x * y * z))
