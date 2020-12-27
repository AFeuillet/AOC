import re

nfile = open('data/day04.txt', 'r')
nbl = nfile.read().split('\n\n')
base = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt', 'cid']
base2 = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']

count = 0
for line in nbl:
	attribs = re.findall(r"[\w]+:[\w\#]+", line)
	if len(attribs) < 7:
		continue

	attribs2 = re.findall(r"[\w]+:", line)
	valid2 = True
	for baseAttr in base2:
		if baseAttr not in attribs2:
			valid2 = False
	if not valid2:
		continue

	valid = True
	for at in attribs:
		ba = at.split(':')
		if ba[0] not in base:
			valid = False
			break
		else:
			if ba[0] == 'byr' and (int(ba[1]) < 1920 or int(ba[1]) > 2002):
				valid = False
				break
			if ba[0] == 'iyr' and (int(ba[1]) < 2010 or int(ba[1]) > 2020):
				valid = False
				break
			if ba[0] == 'eyr' and (int(ba[1]) < 2020 or int(ba[1]) > 2030):
				valid = False
				break
			if ba[0] == 'hgt' and ba[1][-2:] not in ['cm', 'in']:
				valid = False
				break
			if ba[0] == 'hgt' and ba[1][-2:] == 'cm' and (int(ba[1][:-2]) < 150 or int(ba[1][:-2]) > 193):
				valid = False
				break
			if ba[0] == 'hgt' and ba[1][-2:] == 'in' and (int(ba[1][:-2]) < 59 or int(ba[1][:-2]) > 76):
				valid = False
				break
			if ba[0] == 'hcl':
				regex = re.compile('^\#[a-f0-9]{6}$', re.I)
				match = regex.match(str(ba[1]))
				if not match:
					valid = False
					break
			if ba[0] == 'ecl' and ba[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				valid = False
				break
			if ba[0] == 'pid':
				regex = re.compile('^[0-9]{9}$', re.I)
				match = regex.match(str(ba[1]))
				if not match:
					valid = False
					break
	if valid:
		count += 1

print(count)
