nfile = open('data/day03.txt', 'r')
nbl = nfile.read().split('\n')

vgamma = ''
epsil = ''

for i in range(len(nbl[0])):
	gcount = 0
	for con in nbl:
		if con[i] == '1':
			gcount += 1
	if gcount > len(nbl) / 2:
		vgamma += '1'
		epsil += '0'
	else:
		vgamma += '0'
		epsil += '1'
print(int(vgamma, 2) * int(epsil, 2))