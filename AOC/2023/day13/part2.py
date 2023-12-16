nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')


volcano = []
def parseV(volcano, initv):	
	lv = len(volcano)
	for i in range(1, lv):
		if initv == i:
			continue
		if ((i < len(volcano) / 2 and volcano[:i] == list(reversed(volcano[i:2 * i]))) or 
			(i > len(volcano) / 2 and volcano[2 * i - lv:i] == list(reversed(volcano[i:2 * i])))):
			return i
	return 0
	
total = 0

def getBasei(volcano):
	a = parseV(volcano, -1)
	if a != 0:
		return a
	return parseV(list(map(list, zip(*volcano))), -1)

def getNb(volcano, initv):
	a = parseV(volcano, initv) * 100
	if a != 0:
		return a
	return parseV(list(map(list, zip(*volcano))), initv)

def reverseIt(volcano, i, j):
	if volcano[i][j] == '.':
		volcano[i][j] = '#'
	else:
		volcano[i][j] = '.'

def loopin(volcano, initv):
	for i in range(len(volcano)):
		for j in range(len(volcano[i])):
			reverseIt(volcano, i, j)
			a = getNb(volcano, initv)
			if a != 0:
				return a
			reverseIt(volcano, i, j)
	intibase = getNb(volcano, -1)
	if intibase > 99:
		return intibase/100
	return intibase * 100

for nb in nbl:
	if nb == '':
		total += loopin(volcano, getBasei(volcano))
		volcano = []
	else:
		volcano.append(list(nb))

total += loopin(volcano, getBasei(volcano))
print(total)