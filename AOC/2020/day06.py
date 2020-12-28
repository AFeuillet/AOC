nfile = open('data/day06.txt', 'r')
nbl = nfile.read().split('\n\n')

count = 0

for line in nbl:
	lista = set()
	lineb = line.split('\n')
	for letters in lineb:
		for letter in letters:
			lista.add(letter)
	count += len(lista)

print(count)
