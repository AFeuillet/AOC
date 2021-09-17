nfile = open('data/day01.txt', 'r')
nbs = nfile.read()

print("Part one: %s" % (nbs.count('(') - nbs.count(')')))

total = 0
curpos = 0
for par in nbs:
	curpos += 1
	if par == '(':
		total += 1
	else:
		total -= 1
	if total == -1:
		print("Part two: %s" % curpos)
		break


