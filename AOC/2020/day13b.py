nfile = open('data/day13.txt', 'r')
nbl = nfile.read().split('\n')
buses = nbl[1].split(',')

buslist = {}
for i in range(len(buses)):
	if buses[i] == 'x':
		continue
	buslist[int(buses[i])] = -i % int(buses[i]) 
print(buslist)

i = 1
inc = 1
for bus in buslist.keys():
    while i % bus != buslist[bus]:
		i += inc
    inc *= bus
print(i)