nfile = open('data/day08.txt', 'r')
nbl = nfile.read().split('\n')

digits = {
	8: 'abcdefg',	# len 7
	0: 'abcefg',	# len 6
	6: 'abdefg',	# len 6
	9: 'abcdfg',	# len 6
	2: 'acdeg',		# len 5
	3: 'acdfg',		# len 5
	5: 'abdfg',		# len 5
	4: 'bcdf',		# len 4
	7: 'acf',		# len 3
	1: 'cf',		# len 2
}

def partOne():
	total = 0
	for line in nbl:
		signals = line.split(' | ')
		patt = signals[0].split()
		outp = signals[1].split()
		for o in outp:
			if len(o) in [len(digits[1]), len(digits[4]), len(digits[7]), len(digits[8])]:
				total += 1
	return total
#print("Part One: %s" % partOne())

def addval(patt, o, val):
	patt.remove(o)
	vk[val] = o
	kv[''.join(sorted(o))] = str(val)

total = 0
for line in nbl:
	kv = {}
	vk = {}
	signals = line.split(' | ')
	patt = signals[0].split()
	outp = signals[1].split()
	while len(patt) > 0:
		for o in patt:
			leno = len(o)
			if leno == 2:
				addval(patt,o, 1)
			elif leno == 3:
				addval(patt,o, 7)
			elif leno == 4:
				addval(patt,o, 4)
			elif leno == 5:
				if 1 in vk and all(item in o for item in vk[1]):
					addval(patt,o, 3)
				elif 6 in vk and all(item in vk[6] for item in o):
					addval(patt,o, 5)
				elif 1 in vk and 5 in vk:
					addval(patt,o, 2)
			elif leno == 6:
				if 4 in vk and all(item in o for item in vk[4]):
					addval(patt,o, 9)
				elif 1 in vk and 9 in vk and all(item in o for item in vk[1]):
					addval(patt,o, 0)
				elif 9 in vk and 0 in vk:
					addval(patt,o, 6)
			elif leno == 7:
				addval(patt,o, 8)
	outstring = ''
	for o in outp:
		outstring += kv[''.join(sorted(o))]
	total += int(outstring)

print("Part Two: %s" % total)
	