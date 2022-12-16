from os import system
from time import sleep
nbl = open('data.txt').read().split('\n')

caves = []
total = 0
minx, maxx, maxy = float('inf'), 0, 0

def drawit():
	system('clear')
	for c in caves:
		print(c)
	#sleep(0.1)

for iline, line  in enumerate(nbl):		
	l1 = line.split(' -> ')
	for li in l1:
		l2 = li.split(',')
		minx, maxx, maxy = min(int(l2[0]), minx), max(int(l2[0]), maxx), max(int(l2[1]), maxy)


for i in range(maxy + 1):
	caves.append([' ' for j in range(maxx - minx + 1)])

for iline, line  in enumerate(nbl):		
	l1 = line.split(' -> ')
	oldx, oldy = 0, 0
	for li in l1:
		l2 = li.split(',')
		if oldx != 0:
			if oldx == int(l2[0]) and oldy < int(l2[1]):
				for i in range(oldy, int(l2[1]) + 1):
					caves[i][int(l2[0]) - minx] = '#'
			elif oldx == int(l2[0]) and oldy > int(l2[1]):
				for i in range(int(l2[1]), oldy + 1):
					caves[i][int(l2[0]) - minx] = '#'
			elif oldy == int(l2[1]) and oldx < int(l2[0]):
				for i in range(oldx - minx, int(l2[0]) - minx + 1):
					caves[int(l2[1])][i] = '#'
			elif oldy == int(l2[1]) and oldx > int(l2[0]):
				for i in range(int(l2[0]) - minx, oldx - minx + 1):
					caves[int(l2[1])][i] = '#'
		oldx = int(l2[0])
		oldy = int(l2[1])


def drop(x, y):
	if y >= maxy:
		return False
	while True:
		if y >= maxy:
			return False
		caves[y][x] = 'o'
		if caves[y + 1][x] == '#' or caves[y + 1][x] == 'o':
			if caves[y + 1][x - 1] == ' ':
				caves[y][x] = ' '
				return drop(x - 1, y + 1)
			elif caves[y + 1][x + 1] == ' ':
				caves[y][x] = ' '
				return drop(x + 1, y + 1)
			else:
				caves[y][x] = 'o'
			return True
		else:
			caves[y][x] = ' '
		y += 1

it = 0 
while(drop(500 - minx, 0)):
	it += 1
	continue

for c in caves:
	total += c.count('o')

print('Part 1: {}'.format(total))
