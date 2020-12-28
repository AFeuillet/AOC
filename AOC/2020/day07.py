import re

nfile = open('data/day07.txt', 'r')
nbl = nfile.read().split('\n')

count = 0
bags = {}
colorf = "shiny gold"

for line in nbl:
	regex = re.compile("([a-z]+ [a-z]+) bags?", re.I)
	match = regex.findall(line)
	if match[0]:
		bags[match[0]] = []
		if match[1] != 'no other':
			for bg in range(1, len(match)):
				bags[match[0]].append(match[bg])

for bag, value in bags.items():
	if bag != 'shiny gold':
		for minibag in value:
			for mbag in bags[minibag]:
				if mbag not in bags[bag]:
					bags[bag].append(mbag)

for bag, value in bags.items():
	if colorf in value:
		count +=1 

print(count)