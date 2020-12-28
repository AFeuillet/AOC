nfile = open('data/day09.txt', 'r')
nbl = nfile.read().split('\n')

t=0
pos = 25
for line in nbl:
	if t >= pos:
		found = False
		for i in range(t - pos, t):
			for j in range(i, t):
				if i != j and not found:
					if int(line) == int(nbl[i]) + int(nbl[j]):
						found = True
		if not found:
			print("Not found:", line)
			exit()
	t += 1

