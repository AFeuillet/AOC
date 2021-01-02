nfile = open('data/day12.txt', 'r')
nbl = nfile.read().split('\n')

x = y = 0
rosace = 'ENWS'
facing = 0 

def pilote(x, y, way, value):
	if way == 'N':
		y += value
	elif way == 'S':
		y -= value
	elif way == 'E':
		x += value
	elif way == 'W':
		x -= value
	return (x,y)


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

