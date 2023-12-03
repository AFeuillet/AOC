nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

schem = [nb for nb in nbl]

def issymb(c):
	return c != '.' and not c.isdigit()

def issurrended(i, j):
	if i - 1 >= 0:
		if issymb(schem[i - 1][j]):
				return True
		if j - 1 >= 0 and issymb(schem[i - 1][j - 1]):
			return True
		if j + 1 < len(schem[i - 1]) and issymb(schem[i - 1][j + 1]):
			return True
	if j - 1 >= 0 and issymb(schem[i][j - 1]):
		return True
	if j + 1 < len(schem[i]) and issymb(schem[i][j + 1]):
		return True
	if i + 1 < len(schem):
		if issymb(schem[i + 1][j]):
				return True
		if j - 1 >= 0 and issymb(schem[i + 1][j - 1]):
			return True
		if j + 1 < len(schem[i + 1]) and issymb(schem[i + 1][j + 1]):
			return True
	return False

total = 0
tmpint = ''
green = False
for i, line in enumerate(schem):
	for j, c in enumerate(line):
		if c.isdigit():
			tmpint += c
			if issurrended(i, j):
				green = True
		else:
			if green == True:
				total += int(tmpint)
			tmpint = ''
			green = False

print(total)