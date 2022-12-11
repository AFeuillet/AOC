import re

nbl = open('data.txt').read().split('\n')

monkeys = {}
imonkey = 0

reg1c = re.compile(r"Starting items: (.*)")
reg2c = re.compile(r"Operation: new = old (.) (.*)")
reg3c = re.compile(r".* (\d+)")

iloop = 0
for iline, line  in enumerate(nbl):
	if line == '':
		imonkey += 1
		iloop = 0
		continue
	if iloop == 0:
		monkeys[imonkey] = {'items': [], 'op': '', 'div': 1, 'true': 0, 'false': 0, 'inspect': 0}
	elif iloop == 1:
		reg1g = reg1c.findall(line)
		monkeys[imonkey]['items'] = [int(a) for a in reg1g[0].split(',')]
	elif iloop == 2:
		reg2g = reg2c.findall(line)
		monkeys[imonkey]['op'] = reg2g[0]
	elif iloop == 3:
		reg3g = reg3c.findall(line)
		monkeys[imonkey]['div'] = int(reg3g[0])
	elif iloop == 4:
		reg3g = reg3c.findall(line)
		monkeys[imonkey]['true'] = int(reg3g[0])
	elif iloop == 5:
		reg3g = reg3c.findall(line)
		monkeys[imonkey]['false'] = int(reg3g[0])
	iloop += 1

maxloop = 20
for i in range(1, maxloop + 1):
	for m in monkeys.values():
		for item in m['items']:
			wori = 0
			op2 = item if m['op'][1] == 'old' else int(m['op'][1])
			if m['op'][0] == '*':
				wori = item * op2 
			elif m['op'][0] == '+':
				wori = item + op2
			wori = int(wori / 3)
			if(wori % m['div'] == 0):
				monkeys[m['true']]['items'].append(wori)
			else:
				monkeys[m['false']]['items'].append(wori)
			m['inspect'] += 1
		m['items'] = []

insp = [m['inspect'] for m in monkeys.values()]
insp.sort()
for m in monkeys.values():
	print(m)
print('Part 1: {}'.format(insp[-2] * insp[-1]))