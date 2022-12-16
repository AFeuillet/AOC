import re
nbl = open('data.txt').read().split('\n')

minx, maxx, maxy = float('inf'), 0, 0
sensors = []
dists = []
linepos = 2000000

regx = re.compile(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")

for iline, line  in enumerate(nbl):
	find = regx.findall(line)[0]
	s = [int(find[0]), int(find[1])]
	b = [int(find[2]), int(find[3])]
	d = abs(b[0] - s[0]) + abs(b[1] - s[1])
	if s[1] + d >= linepos and s[1] - d <= linepos:
		sensors.append(s)
		dists.append(d)
	minx, maxx, maxy = min([s[0], b[0], minx]), max([s[0], b[0], maxx]), max([s[1], b[1], maxy])
line10 = ['.' for j in range(maxx + maxy * 2)]
for isens, sensor in enumerate(sensors):
	sx = sensor[0] + maxy
	sy = sensor[1]
	r = dists[isens] - abs(linepos - sensor[1])
	for i in range(sx, sx + r + 1):
		line10[i] = '#'
	for i in range(sx, sx - (r + 1), -1):
		line10[i] = '#'				

print('Part 1: {}'.format(line10.count('#') - 1))