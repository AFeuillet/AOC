nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

schem = [nb for nb in nbl]
curGear = [0, 0]
gears = {} # format (1,2): 


def issymb(c):
	return c == '*'

def surrended(i, j, gg):
	if i - 1 >= 0:
		if issymb(schem[i - 1][j]):
			gg.add((i - 1, j))
		if j - 1 >= 0 and issymb(schem[i - 1][j - 1]):
			gg.add((i - 1, j - 1))
		if j + 1 < len(schem[i - 1]) and issymb(schem[i - 1][j + 1]):
			gg.add((i - 1, j + 1))
	if j - 1 >= 0 and issymb(schem[i][j - 1]):
		gg.add((i , j - 1))
	if j + 1 < len(schem[i]) and issymb(schem[i][j + 1]):
		gg.add((i , j + 1))
	if i + 1 < len(schem):
		if issymb(schem[i + 1][j]):
				gg.add((i + 1, j))
		if j - 1 >= 0 and issymb(schem[i + 1][j - 1]):
			gg.add((i + 1, j - 1))
		if j + 1 < len(schem[i + 1]) and issymb(schem[i + 1][j + 1]):
			gg.add((i + 1, j + 1))
	return gg

total = 0
tmpint = ''
gg = set()
for i, line in enumerate(schem):
	for j, c in enumerate(line):
		if c.isdigit():
			tmpint += c
			gg = surrended(i, j, gg)
		else:
			if gg:
				for g in gg:
					if g not in gears:
						gears[g] = []
					gears[g].append(int(tmpint))
			tmpint = ''
			gg = set()

for k, v in gears.items():
	if len(v) == 2:
		total += v[0] * v[1]
print(total)