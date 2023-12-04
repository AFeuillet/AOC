import re

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

nbi = 10
scrashes = {}

for nb in nbl:
	alln = re.findall(r'(\d+)', nb)
	matchlen = len(list(set(alln[1:nbi + 1]) & set(alln[nbi + 1:])))
	card = int(alln[0])
	scrashes[card] = {
		'count': 0,
		'next': [card + i + 1 for i in range(matchlen)]
		}

def parcours(pid):
	if pid in scrashes:
		scrashes[pid]['count'] += 1
		for nex in scrashes[pid]['next']:
			parcours(nex)
	else:
		scrashes[pid] = {'count': 1, 'next': []}
	return
for i in range(len(scrashes)):
	parcours(i + 1)

total = 0
for s in scrashes.values():
	total += s['count']
print(total)