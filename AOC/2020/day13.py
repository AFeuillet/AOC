nfile = open('data/day13.txt', 'r')
nbl = nfile.read().split('\n')

ts = int(nbl[0])
buses = nbl[1].split(',')
nearest = 100000
busid = 0
for bus in buses:
	if bus == 'x':
		continue
	n = 0
	while True:
		hour = int(bus) * n
		if hour > ts:
			if nearest > hour - ts:
				nearest = hour - ts
				busid = int(bus)
			break
		n += 1
print((busid, nearest, (busid * nearest)))