nfile = open('data/day02.txt', 'r')
nbl = nfile.read().split('\n')

valid = 0
for line in nbl:
	tab = line.split(':')
	(nb, letter) = tab[0].split(' ')
	(mina, maxa) = nb.split('-')
	text = tab[1].replace(' ', '')
	validate = False
	if(text[int(mina) - 1] == letter):
		validate = True
	if(text[int(maxa) - 1] == letter):
		if validate:
			validate = False
		else:
			validate = True
	if validate:
		valid +=1
print(valid)