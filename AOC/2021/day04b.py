nfile = open('data/day04.txt', 'r')
nbl = nfile.read().split('\n')

lotos = []
i = 0
for index, line in enumerate(nbl):
	if index == 0:
		numbs = [int(a) for a in line.split(',')]
	elif line == '':
		lotos.append([])
		i += 1
	else:
		lotos[i - 1].append([int(a) for a in line.split()])

def iswin(loto, num):
	for i in range(len(loto)):
		found = True
		for j in range(len(loto)):
			if loto[i][j] not in num:
				found = False
				break
		if found:
			return True
		found = True
		for j in range(len(loto)):
			if loto[j][i] not in num:
				found = False
				break
		if found:
			return True
	return False

lot = list(range(len(lotos)))


for i in range(len(lotos[0]), len(numbs)):
	tmplot = numbs[:i]
	print(numbs[i])
	newlot = []
	for index, loto in enumerate(lotos):
		thewinnner = iswin(loto, tmplot)
		if thewinnner == False:
			newlot.append(loto)
		else:
			lastwin = loto
	if len(newlot) == 0:
		break
	else:
		lotos = newlot

toto = 0
for i in range(len(lastwin)):
	for j in range(len(lastwin)):
		if lastwin[i][j] not in tmplot:
			toto += lastwin[i][j]
print(toto * tmplot[-1])

