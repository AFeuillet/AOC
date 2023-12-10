import re
from math import lcm

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

dirc = nbl.pop(0)
nbl.pop(0)

dirdict = {}
chmins = {}
startd = []
for nb in nbl:
	allp = re.findall(r'([A-Z|\d]{3})', nb)
	dirdict[allp[0]] ={'L': allp[1], 'R': allp[2]}
	if allp[0][2] == 'A':
		startd.append(allp[0])
		chmins[allp[0]] = {
			'cur': allp[0],
			'pth': [],
			'loopd': 0,
			'zfindpos': []
		}

def thisistheend(pos):
	ennd = True
	for i, st in enumerate(startd):
		startd[i] = dirdict[st][dirc[pos]]
		if startd[i][2] != 'Z':
			ennd = False
	return ennd

pos = 0
total = 1
zztop = []
while(True):
	alllooped = True
	for chmin in chmins.values():
		if chmin['loopd'] == 0:
			alllooped = False
			nxt = dirdict[chmin['cur']][dirc[pos]]
			key = str(chmin['cur'] + '' + str(pos))
			if chmin['cur'][2] == 'Z':
				chmin['zfindpos'].append(total - 1)
				zztop.append(total - 1)
			if key not in chmin['pth']:
				chmin['pth'].append(key)
			else:
				chmin['loopd'] = total
				chmin['pth'] = []
			chmin['cur'] = nxt
	if alllooped:
		break
	if pos + 1 == len(dirc):
		pos = 0
	else:
		pos += 1
	total += 1

print(lcm(zztop[0], zztop[1], zztop[2], zztop[3], zztop[4], zztop[5]))

	