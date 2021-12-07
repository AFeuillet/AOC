nfile = open('data/day01.txt', 'r')
nbl = nfile.read().split('\n')
nbi = [int(a) for a in nbl]

def dayOnea():
	prevone = None
	total = 0
	for n in nbi:
		if prevone != None and n > prevone:
			total += 1
		prevone = n
	return total

print(dayOnea())

def dayOneb():
	prevone = None
	total = 0
	for i in range(2, len(nbi)):
		n = nbi[i - 2] + nbi[i - 1] + nbi[i]
		if prevone != None and n > prevone:
			total += 1
		prevone = n
	return total


print(dayOneb())