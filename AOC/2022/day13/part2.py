nbl = open('data.txt').read().split('\n')

c1, c2, i, index, total = 0, 0, 0, 0, 0

def compare(c1, c2):
	if len(c1) == 0 and len(c2) > 0:
		return True
	elif len(c1) > 0 and len(c2) == 0:
		return False
	for i, vald1 in enumerate(c1):
		if i >= len(c2):
			return False
		vald2 = c2[i]
		if isinstance(vald1, list) or isinstance(vald2, list):
			if not isinstance(vald1, list):
				r = compare([vald1], vald2)
			elif not isinstance(vald2, list):
				r = compare(vald1, [vald2])
			else:
				r = compare(vald1, vald2)
			if r is not None:
				return r
		elif vald1 < vald2:
			return True
		elif vald1 > vald2:
			return False
	if len(c1) > len(c2):
		return False
	elif len(c1) < len(c2):
		return True
	return None

order = [[2], [6]]
for iline, line  in enumerate(nbl):
	if line == '':
		continue
	inserted = False
	for iorder, vald in enumerate(order):
		if compare(eval(line), vald):
			order.insert(iorder, eval(line))
			inserted = True
			break
	if inserted == False:
		order.append(eval(line))

print('Part 2: {}'.format((order.index([2]) + 1 ) * (order.index([6]) + 1 )))