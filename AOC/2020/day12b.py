import math


nfile = open('data/day12.txt', 'r')
nbl = nfile.read().split('\n')

x = y = 0
rosace = 'ENWS'
facing = 0 
xwp = 10
ywp = 1

def pilote(xwp, ywp, way, value):
	if way == 'N':
		ywp += value
	elif way == 'S':
		ywp -= value
	elif way == 'E':
		xwp += value
	elif way == 'W':
		xwp -= value
	return (xwp, ywp)

def wpilote(x, y,xwp, ywp, way, value):
	y = value * ywp
	x = value * xwp
	return (x,y)

for line in nbl:
	c = line[:1]
	value = int(line[1:])
	if c == 'R':
		co = round(math.cos(math.radians(value)))
		si = round(math.sin(math.radians(value)))
		ox = xwp
		oy = ywp
		xwp = ox * co+ oy * si
		ywp = -ox * si+ oy * co
	elif c == 'L':
		co = round(math.cos(math.radians(value)))
		si = round(math.sin(math.radians(value)))
		ox = xwp
		oy = ywp
		xwp = ox * co - oy * si
		ywp = ox * si + oy * co
	elif c == 'F':
		x += value * xwp
		y += value * ywp
	else:
		xwp, ywp = pilote(xwp, ywp, c, value)

print("x: %s, y:%s = %s"%(x,y, abs(x) + abs(y)))

