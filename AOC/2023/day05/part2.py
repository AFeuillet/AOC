nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

seeds = []
chains = []

seeds = [int(n) for n in nbl.pop(0).split(': ')[1].split(' ')]
seedr = []
for i in range(0, len(seeds), 2):
	seedr.append([seeds[i], seeds[i] + seeds[i + 1] - 1])
nbl.pop(0)
mm = []
for nb in nbl:
	if nb and nb[0].isdigit():
		cc = nb.split(' ')
		mm.append([int(cc[1]), int(cc[1]) + int(cc[2]) - 1, int(cc[0]), int(cc[0]) + int(cc[2]) - 1])
	elif nb == '':
		chains.append(mm)
		mm = []

ranginit = seedr
for chain in chains:
	rangenext = []
	for subc in chain:
		rangenw = []
		for rangej in ranginit:
			mina = rangej[0]
			maxa = rangej[1]
			minb = subc[0]
			maxb = subc[1]
			diff = subc[2] - subc[0]

			if mina >= minb and maxa <= maxb:
				rangenext.append([subc[2] + (mina - minb), subc[2] + (mina - minb) + (maxa - mina)])
			elif mina < minb and maxa > maxb:
				rangenw.append([mina, minb - 1])
				rangenext.append([subc[2], subc[3]])
				rangenw.append([maxb + 1, maxa])
			elif mina >= minb and mina < maxb and maxa > maxb:
				rangenext.append([subc[2]  + (mina - minb), subc[3]])
				rangenw.append([maxb + 1, maxa])
			elif mina < minb and maxa > minb and maxa <= maxb:
				rangenext.append([subc[2], maxa + diff])
				rangenw.append([mina, minb - 1])
			else:
				rangenw.append(rangej)
		ranginit = rangenw
	rangenext += rangenw
	ranginit = rangenext

minn = 9999999999
for r in rangenext:
	minn = min(minn, r[0])

print(minn)






