nbl = open('data.txt').read().split('\n')
subtotal = 0
elves = []
for nb in nbl:
	if nb == '':
		elves.append(subtotal)
		subtotal = 0
	else:
		subtotal += int(nb)
elves.sort()
print('Part 1: {}, Part 2: {}'.format(elves[-1], sum(elves[-3:])))