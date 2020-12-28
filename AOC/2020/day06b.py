nfile = open('data/day06.txt', 'r')
nbl = nfile.read().split('\n\n')

count = 0

for line in nbl:
	lista = list()
	lineb = line.split('\n')
	init = True
	for linez in lineb:
		listb = list()
		if init == True:
			lista = list(linez)
		else:
			for l in lista:
				if l in linez:
					listb.append(l)
			lista = listb
		init = False
	count += len(lista)

print(count)
