import re

nfile = open('data/day05.txt', 'r')
nbl = nfile.read().split('\n')

windsiz = 1000
champs = [[0 for x in range(windsiz)] for y in range(windsiz)]

def printchamp():
	for i in range(windsiz):
		for j in range(windsiz):
			if champs[j][i] == 0:
				print('.', end ='')
			else:
				print(champs[j][i], end ='')
		print()

r = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
for line in nbl:
	x0, y0, x1, y1 = [int(a) for a in r.findall(line)[0]]
	if x0 == x1:
		ys, ye = (y0, y1) if y0 < y1 else (y1, y0)
		for y in range(ys, ye + 1):
			champs[x0][y] += 1 
	elif y0 == y1:
		xs, xe = (x0, x1) if x0 < x1 else (x1, x0)
		for x in range(xs, xe + 1):
			champs[x][y0] += 1 
	else:
		x, y = (x0, y0)
		for i in range(abs(x0 - x1)):
			champs[x][y] += 1
			x = x + 1 if x0 < x1 else x - 1
			y = y + 1 if y0 < y1 else y - 1
		champs[x][y] += 1

total = 0
for i in range(windsiz):
	for j in range(windsiz):
		if champs[j][i] >= 2:
			total += 1

printchamp()
print(total)