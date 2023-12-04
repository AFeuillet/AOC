import re

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

nbi = 10
total = 0
for nb in nbl:
	alln = re.findall(r'(\d+)', nb)
	matchlen = len(list(set(alln[1:nbi + 1]) & set(alln[nbi + 1:]))) - 1
	if matchlen >= 0:
		total += 2 ** matchlen

print(total)
