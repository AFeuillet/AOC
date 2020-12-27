nfile = open('data/day02.txt', 'r')
nbl = nfile.read().split('\n')

valid = 0
for line in nbl:
	tab = line.split(':')
	(nb, letter) = tab[0].split(' ')
	(mina, maxa) = nb.split('-')
	text = tab[1].replace(' ', '')
	count = 0 
	for let in text:
		if let == letter:
			count += 1
	if count >= int(mina) and count <= int(maxa):
		valid += 1
print(valid)