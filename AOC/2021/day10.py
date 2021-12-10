nfile = open('data/day10.txt', 'r')
nbl = nfile.read().split('\n')

total_part1 = 0
total2 = []
for line in nbl:
	total_part2 = 0
	opener = []
	for i, c in enumerate(line):
		if c in ['{', '[', '<', '(']:
			opener.append(c)
		else:
			if (
				(c == '}' and opener[-1] == '{') or
				(c == ')' and opener[-1] == '(') or
				(c == ']' and opener[-1] == '[') or 
				(c == '>' and opener[-1] == '<')
				):
				opener.pop()
			else:
				if c == '}':
					total_part1 += 1197
				elif c == ')':
					total_part1 += 3
				elif c == ']':
					total_part1 += 57
				elif c == '>':
					total_part1 += 25137
				break
		if i == len(line) - 1:
			for o in reversed(opener):
				total_part2 *= 5
				if o == '{':
					total_part2 += 3
				elif o == '(':
					total_part2 += 1
				elif o == '[':
					total_part2 += 2
				elif o == '<':
					total_part2 += 4
			total2.append(total_part2)

print("Part One: %s" % total_part1)
print("Part Two: %s" % sorted(total2)[int(len(total2) / 2)])