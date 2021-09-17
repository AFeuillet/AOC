import re

nfile = open('data/day07.txt', 'r')
nbl = nfile.read().split('\n')
r = re.compile(r'(.*) -> (.*)')

def checkint(tables, action):
	asc = action[0].split(' ')
	x = -1
	y = -1
	if asc[0] in tables:
		x = tables[asc[0]]
	elif asc[0].isnumeric():
		x = int(asc[0])
	if asc[2] in tables:
		y = tables[asc[2]]
	elif asc[2].isnumeric():
		y = int(asc[2])
	return (x, y)

tables = {}
actions = []
for untre in nbl:
	grp = r.findall(untre)[0]
	action = grp[0]
	val = grp[1]
	actions.append((action, val))

for i in range(len(actions)):
	for action in actions:
		if 'AND' in action[0] or 'OR' in action[0] or 'LSHIFT' in action[0] or 'RSHIFT' in action[0]:
			x, y = checkint(tables, action)
			if x != -1 and y != -1:
				if 'AND' in action[0]:
					tables[action[1]] = int(x & y)
				elif 'OR' in action[0]:
					tables[action[1]] = int(x | y)
				elif 'LSHIFT' in action[0]:
					tables[action[1]] = int(x << y)
				elif 'RSHIFT' in action[0]:
					tables[action[1]] = int(x >> y)
				actions.remove(action)
		elif 'NOT' in action[0]:
			asc = action[0].split(' ')
			if asc[1] in tables:
				tables[action[1]] = 65535 - tables[asc[1]]
				actions.remove(action)
			elif asc[1].isnumeric():
				tables[action[1]] = 65535 - int(asc[1])
				actions.remove(action)
		else:
			if action[0] in tables:
				tables[action[1]] = tables[action[0]]
				actions.remove(action)
			elif action[0].isnumeric():
				tables[action[1]] =int(action[0])
				actions.remove(action)
	if len(actions) == 0:
		print("Part One: %s" % tables['a'])
		break

biga = tables['a']
tables = {}
actions = []
for untre in nbl:
	grp = r.findall(untre)[0]
	action = grp[0]
	val = grp[1]
	actions.append((action, val))

for i in range(len(actions)):
	for action in actions:
		if 'AND' in action[0] or 'OR' in action[0] or 'LSHIFT' in action[0] or 'RSHIFT' in action[0]:
			x, y = checkint(tables, action)
			if x != -1 and y != -1:
				if 'AND' in action[0]:
					tables[action[1]] = int(x & y)
				elif 'OR' in action[0]:
					tables[action[1]] = int(x | y)
				elif 'LSHIFT' in action[0]:
					tables[action[1]] = int(x << y)
				elif 'RSHIFT' in action[0]:
					tables[action[1]] = int(x >> y)
				actions.remove(action)
		elif 'NOT' in action[0]:
			asc = action[0].split(' ')
			if asc[1] in tables:
				tables[action[1]] = 65535 - tables[asc[1]]
				actions.remove(action)
			elif asc[1].isnumeric():
				tables[action[1]] = 65535 - int(asc[1])
				actions.remove(action)
		else:
			if action[1] == 'b':
				tables[action[1]] = biga
				actions.remove(action)
			elif action[0] in tables:
				tables[action[1]] = tables[action[0]]
				actions.remove(action)
			elif action[0].isnumeric():
				tables[action[1]] =int(action[0])
				actions.remove(action)
	if len(actions) == 0:
		print("Part Two: %s" % tables['a'])
		break