nfile = open('data/day10.txt', 'r')
nbl = nfile.read().split('\n')

total_part1 = 0
total2 = []
closes = {
	'}': {'value': 1197, 'op': '{'},
	')': {'value': 3, 'op': '('},
	']': {'value': 57, 'op': '['},
	'>': {'value': 25137, 'op': '<'}
	}
opens = {'{': 3, '(': 1, '[': 2, '<': 4}
for line in nbl:
	total_part2 = 0
	opener = []
	for i, c in enumerate(line):
		if c in opens.keys():
			opener.append(c)
		else:
			if c in closes.keys() and opener[-1] == closes[c]['op']:
				opener.pop()
			else:
				total_part1 += closes[c]['value']
				break
		if i == len(line) - 1:
			for o in reversed(opener):
				total_part2 *= 5
				total_part2 += opens[o]
			total2.append(total_part2)

print("Part One: %s" % total_part1)
print("Part Two: %s" % sorted(total2)[int(len(total2) / 2)])