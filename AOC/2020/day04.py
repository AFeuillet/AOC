import re

nfile = open('data/day04.txt', 'r')
nbl = nfile.read().split('\n\n')
base = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']

count = 0
for line in nbl:
	attribs = re.findall(r"[\w]+:", line)
	valid = True
	for baseAtt in base:
		if baseAtt not in attribs:
			valid = False
	if valid:
		count += 1
print(count)
