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
		'count': 1,
		'next': [card + i + 1 for i in range(matchlen)]
		}

total = 0
for i in range(len(scrashes)):
	if i + 1 in scrashes:
		total += scrashes[i + 1]['count']
		for nex in scrashes[i + 1]['next']:
			scrashes[nex]['count'] += scrashes[i + 1]['count']

print(total)