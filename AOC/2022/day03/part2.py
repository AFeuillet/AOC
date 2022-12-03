import string
nbl = open('data.txt').read().split('\n')
alpha = string.ascii_letters

total = 0
elfegroup = []
for nb in nbl:
	elfegroup.append(nb)
	if len(elfegroup) == 3:
		dup1 = list(set(elfegroup[0]) & set(elfegroup[1]) & set(elfegroup[2]))[0]
		elfegroup = []
		total += alpha.index(dup1) + 1
		continue

print('Part 2: {}'.format(total))