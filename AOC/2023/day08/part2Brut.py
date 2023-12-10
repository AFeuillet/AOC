import re

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')


dirc = nbl.pop(0)
nbl.pop(0)

dirdict = {}
startd = []
for nb in nbl:
	allp = re.findall(r'([A-Z|\d]{3})', nb)
	dirdict[allp[0]] ={'L': allp[1], 'R': allp[2]}
	if allp[0][2] == 'A':
		startd.append(allp[0])

def thisistheend(pos):
	ennd = True
	for i, st in enumerate(startd):
		startd[i] = dirdict[st][dirc[pos]]
		if startd[i][2] != 'Z':
			ennd = False
	return ennd

pos = 0
total = 1
while(not thisistheend(pos)):
	if pos + 1 == len(dirc):
		pos = 0
	else:
		pos += 1
	total += 1

print(total)