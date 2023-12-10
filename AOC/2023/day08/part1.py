import re

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')


dirc = nbl.pop(0)
nbl.pop(0)

dirdict = {}
for nb in nbl:
	allp = re.findall(r'([A-Z]{3})', nb)
	dirdict[allp[0]] ={'L': allp[1], 'R': allp[2]}

curd = 'AAA'
pos = 0
total = 0
while(curd != 'ZZZ'):
	curd = dirdict[curd][dirc[pos]]
	if pos + 1 == len(dirc):
		pos = 0
	else:
		pos += 1
	total += 1
print(total)