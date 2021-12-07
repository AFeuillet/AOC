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

def iswin(num):
	for index, loto in enumerate(lotos):
		for i in range(len(loto)):
			found = True
			for j in range(len(loto)):
				if loto[i][j] not in num:
					found = False
					break
			if found:
				return index
			found = True
			for j in range(len(loto)):
				if loto[j][i] not in num:
					found = False
					break
			if found:
				return index
	return -1

nbppar = len(lotos)
for i in range(len(lotos[0]), len(numbs)):
	tmplot = numbs[:i]
	thewinnner = iswin(tmplot)
	if thewinnner != -1:
		break

toto = 0
for i in range(len(lotos[thewinnner])):
	for j in range(len(lotos[thewinnner])):
		if lotos[thewinnner][i][j] not in tmplot:
			toto += lotos[thewinnner][i][j]
print(toto * tmplot[-1])