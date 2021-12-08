import math
nfile = open('data/day07.txt', 'r')
banc = [int(a) for a in nfile.read().split(',')]

part = 2

cheapest = float('inf')
the = -1
for i in range(max(banc) + 1):
	total = 0
	for poi in banc:
		if part == 1:
			total += abs(poi - i)
		else:
			total += sum(range(abs(poi - i) + 1))
		if total > cheapest:
			break
	if total < cheapest:
		cheapest = total
		the = i
print(cheapest, the)