nfile = open('data/day03.txt', 'r')
nbl = nfile.read()


def get_pos(c, x, y):
	if c == '>':
		x += 1
	elif c == '<':
		x -= 1
	elif c == '^':
		y += 1
	elif c == 'v':
		y -= 1
	return x, y

x = 0
y = 0
houses = set()
for c in nbl:
	houses.add((x, y))
	x, y = get_pos(c, x, y)
print("Part One: %s" % (len(houses))) 

x = 0
y = 0
xr = 0
yr = 0
houses_santa = set()
houses_robot = set()
houses_santa.add((0,0))
index = 0
for c in nbl:
	if index % 2 == 0:
		x, y = get_pos(c, x, y)
		houses_santa.add((x, y))
	else:
		xr, yr = get_pos(c, xr, yr)
		houses_robot.add((xr, yr))
		
	index += 1
print("Part Two: %s" % (len(houses_santa.union(houses_robot))))