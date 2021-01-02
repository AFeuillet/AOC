from os import system
from time import sleep

nfile = open('data/day12.txt', 'r')
nbl = nfile.read().split('\n')

x = y = 0
rosace = 'ENWS'
facing = 0 

def pilote(x, y, way, value):
	#print(way)
	oldx = x
	oldy = y
	if way == 'N':
		y += value
		bd = u'\u25B2'
	elif way == 'S':
		y -= value
		bd = u'\u25BC'
	elif way == 'E':
		x += value
		bd = u'\u25b6'
	elif way == 'W':
		x -= value
		bd = u'\u25C0'

	pas = 1
	if x != oldx:
		if oldx > x:
			pas = -1
		for i in range(oldx, x, pas):
			system('clear')
			print('\n' * (oldy + 30))
			print(' ' * (i + 100) + bd)
			sleep(0.001)
	pas = 1
	if y != oldy:
		if oldy > y:
			pas = -1
		for i in range(oldy, y, pas):
			system('clear')
			print('\n' * (i + 30))
			print(' ' * (oldx + 100) + bd)
			sleep(0.001)

	return (x,y)

system('clear')
for line in nbl:
	c = line[:1]
	value = int(line[1:])

	if c == 'R':
		d = (value / 90) % 4
		facing -= d
		if facing <= -1:
			facing = 4 + facing
	elif c == 'L':
		d = (value / 90) % 4
		facing += d
		if facing >= 4:
			facing = facing - 4
	elif c == 'F':
		x, y = pilote(x, y, rosace[facing], value)
	else:
		x, y = pilote(x, y, c, value)

print("x: %s, y:%s = %s"%(x,y, abs(x) + abs(y)))

