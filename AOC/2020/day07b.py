import re

nfile = open('data/day07.txt', 'r')
nbl = nfile.read().split('\n')


count = 0
bags = {}

for line in nbl:
	regex = re.compile("([0-9]*)\s?([a-z]+ [a-z]+) bags?", re.I)
	match = regex.findall(line)	
	if match[0]:
		bags[match[0][1]] = []
		if match[1] != 'no other':
			for bg in range(1, len(match)):
				bags[match[0][1]].append(match[bg])


def qtte(color):
	total = 0
	for bag in bags[color]:
		if bag[0] == '':
			return 0
		qte = int(bag[0])
		total += qte
		total += qte * qtte(bag[1])
	return total

print(qtte("shiny gold"))