nfile = open('data/day10.txt', 'r')
nbl = nfile.read().split('\n')
nbi = [int(a) for a in nbl]
rnbi = sorted(nbi)

val = 0
one = 0
three = 0
for line in sorted(nbi):
	if line - val < 3:
		one += line - val
		val = line
	elif line - val == 3:
		three += 1
		val = line
three += 1
print(one * three)