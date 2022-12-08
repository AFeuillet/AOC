import re
nbl = open('data.txt').read().split('\n')

cdex = r"cd (.+)"
fileex = r"(\d+) (.+)"
directories = {}
pos = 0
total = 0
maxi = 100000

def addtoTotal(value):
	global total
	if value < maxi:
		total += value

def recur():
	global pos
	subtotal = 0
	while pos < len(nbl):
		rdir = re.compile(cdex)
		grpdir = rdir.findall(nbl[pos])
		if len(grpdir) > 0:
			if grpdir[0] == '..':
				addtoTotal(subtotal)
				return subtotal
			else:
				pos += 1
				directories[grpdir[0]] = recur()
				if directories[grpdir[0]] is not None:
					subtotal += directories[grpdir[0]]
		else:
			rfile = re.compile(fileex)
			grp = rfile.findall(nbl[pos])
			if len(grp) > 0:
				subtotal += int(grp[0][0])
		pos += 1
	if pos == len(nbl):
		addtoTotal(subtotal)
		return subtotal
	return subtotal


recur()
print('Part 1: {}'.format(total))

valss = list(directories.values())
valss.sort()
for val in valss:
	if 70000000 - (directories['/'] - val) >= 30000000:
		print('Part 2: {}'.format(val))
		exit()
