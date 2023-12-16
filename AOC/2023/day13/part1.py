nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')


volcano = []
def parseV(volcano):
	lv = len(volcano)
	for i in range(1, lv):
		if ((i < len(volcano) / 2 and volcano[:i] == list(reversed(volcano[i:2 * i]))) or 
			(i > len(volcano) / 2 and volcano[2 * i - lv:i] == list(reversed(volcano[i:2 * i])))):
			return i
	return 0
total = 0
for nb in nbl:
	if nb == '':
		total += parseV(list(map(list, zip(*volcano))))
		total += parseV(volcano) * 100
		volcano = []
	else:
		volcano.append(list(nb))
total += parseV(list(map(list, zip(*volcano))))
total += parseV(volcano) * 100

print(total)