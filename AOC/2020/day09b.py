nfile = open('data/day09b.txt', 'r')
nbl = nfile.read().split('\n')

invalid = 167829540
mina = 9999999
maxa = 0

for i in range(0, len(nbl)):
	suma = 0 
	for j in range(i, len(nbl)):
		suma += int(nbl[j])
		if int(suma) > invalid:
			break
		if suma == invalid:
			for k in range(i, j):
				mina = min(mina, int(nbl[k]))
				maxa = max(maxa, int(nbl[k]))
			print("Find: min:%s max:%s total:%s"%(mina, maxa, mina + maxa))
			exit()
