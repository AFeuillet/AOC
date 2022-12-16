import re
nbl = open('data.txt').read().split('\n')

minx, maxx, maxy = float('inf'), 0, 0
sensors = []
dists = []
	
regx = re.compile(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")

for iline, line  in enumerate(nbl):
	find = regx.findall(line)[0]
	s = [int(find[0]), int(find[1])]
	b = [int(find[2]), int(find[3])]
	d = abs(b[0] - s[0]) + abs(b[1] - s[1])
	sensors.append(s)
	dists.append(d)
	minx, maxx, maxy = min([s[0], b[0], minx]), max([s[0], b[0], maxx]), max([s[1], b[1], maxy])

coormax = 4000000
#coormax = 20

def fulline(lin):
	if lin[0][0] != 0:
		return False
	maxi = lin[0][1]
	for i in range(1, len(lin)):
		maxi = max(maxi, lin[i - 1][1])
		if lin[i][0] > maxi:
			return maxi
	return True

for iline in range(coormax):
	linepos = iline
	segms = []
	for isens, sensor in enumerate(sensors):
		sx = sensor[0]
		sy = sensor[1]
		if sy + dists[isens] >= linepos and sy - dists[isens] <= linepos:	
			r = dists[isens] - abs(linepos - sensor[1])
			sxm = sx + r + 1 if sx + r + 1 < coormax + 1 else coormax + 1
			sxn = sx - (r + 1) if sx - (r + 1) >= 0 else -1
			segms.append([sxn + 1, sxm])
	val = fulline(sorted(segms))
	if val != True:
		print('Part 1: {}'.format((val * 4000000) + linepos))
		exit()
