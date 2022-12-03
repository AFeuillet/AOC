import string
nbl = open('data.txt').read().split('\n')
alpha = string.ascii_letters

total = 0
for nb in nbl:
	dup1 = list(set(nb[:int(len(nb)/2)]) & set(nb[int(len(nb)/2):]))[0]
	total += alpha.index(dup1) + 1

print('Part 1: {}'.format(total))