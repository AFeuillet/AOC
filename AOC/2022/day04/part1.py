nbl = open('data.txt').read().split('\n')

total = 0
for nb in nbl:
	elves = nb.split(',')
	elve1 = elves[0].split('-')
	elve2 = elves[1].split('-')
	if ((int(elve1[0]) >= int(elve2[0]) and int(elve1[1]) <= int(elve2[1])) or 
		(int(elve1[0]) <= int(elve2[0]) and int(elve1[1]) >= int(elve2[1]))):
		total += 1

print('Part 1: {}'.format(total))