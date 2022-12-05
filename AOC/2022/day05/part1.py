import re
import string
nbl = open('data.txt').read().split('\n')
alpha = string.ascii_letters


size = 9
ship = [[] for i in range(size)] 

movec = False
for nb in nbl:
	if nb == '':
		movec = True
		for i in range(size):
			ship[i].reverse()
	elif movec == False:
		index = 0
		for c in range(0, len(nb), 1):
			if nb[c] in alpha:
				ship[index // 4].append(nb[c])
			index += 1
	else:
		r = re.compile(r"move (\d+) from (\d+) to (\d+)")
		nbcrave, dest1, dest2 = r.findall(nb)[0]
		for i in range(int(nbcrave)):
			ship[int(dest2) - 1].append(ship[int(dest1) - 1].pop())

result = ''
for i in range(size):
	result += ship[i].pop()

print('Part 1: {}'.format(result))