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

for iline, line  in enumerate(nbl):		
	if i == 0:
		c1 = eval(line)
	elif i == 1:
		c2 = eval(line)
	elif i == 2:
		i = -1
		index += 1
		if compare(c1, c2) == True:
			total += index
	i += 1

print('Part 1: {}'.format(total))
