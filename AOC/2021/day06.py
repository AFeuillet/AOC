nfile = open('data/day06.txt', 'r')
banc = [int(a) for a in nfile.read().split(',')]

days = 256
def firstSolution():
	for day in range(days):
		for i in range(len(banc)):
			if banc[i] > 0:
				banc[i] -= 1
			else:
				banc[i] = 6
				banc.append(8)
	return len(banc)

def secondSolution():
	paquet  = [0 for x in range(10)]
	for poipoi in banc:
		paquet[poipoi] += 1
	for day in range(days):
		paquet[7] += paquet[0]
		paquet[9] += paquet[0]
		for i in range(0, 9):
			paquet[i] = paquet[i + 1]
		paquet[9] = 0
	total = 0
	for paaq in paquet:
		total += paaq
	return total

print(secondSolution())