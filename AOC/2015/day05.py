nfile = open('data/day05.txt', 'r')
nbl = nfile.read().split('\n')

voyels = ['a', 'e', 'i', 'o', 'u']
bads = ['ab', 'cd', 'pq', 'xy']

total = 0
for word in nbl:
	voyelcount = 0
	twiced = False
	cool = True
	previous = ''
	for c in word:
		if c in voyels:
			voyelcount += 1
		if previous == c:
			twiced = True
		if previous + c in bads:
			cool = False
			break
		previous = c
	if cool and voyelcount >= 3 and twiced:
		total += 1
print("Part One: %s" % total)

total = 0
for word in nbl:
	paired = False
	mirrored = False
	sett = set()
	if len(word) > 0:
		sett.add((word[0], word[1]))
	for i in range(len(word)):
		if i > 1 and (word[i] != word[i - 1] or word[i - 1] != word[i - 2]):
			if (word[i - 1], word[i]) in sett:
				paired = True
			else:
				sett.add((word[i - 1], word[i]))
		if i >= 2 and word[i] == word[i - 2]:
			mirrored = True
		if i >= 3 and word[i] == word[i - 1] and word[i] == word[i - 2] and word[i] == word[i - 3]:
			paired = True
			mirrored = True
			break
	if paired and mirrored:
		total += 1
print("Part Two: %s" % total)

