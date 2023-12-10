nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

fields = []
loopi = []
startp = (0, 0)

def getNexit():
	last = loopi[len(loopi) - 2]
	cur = loopi[len(loopi) - 1]
	i, j = cur[0], cur[1]
	elt = fields[i][j]

	nwone = (0, 0)
	if elt == '-':
		nwone = (i, j + 1) if (i, j - 1) == last else (i, j - 1)
	elif elt == '|':
		nwone = (i + 1, j) if (i - 1, j) == last else (i - 1, j)
	elif elt == 'L':
		nwone = (i, j + 1) if (i - 1, j) == last else (i - 1, j)
	elif elt == 'J':
		nwone = (i, j - 1) if (i - 1, j) == last else (i - 1, j)
	elif elt == '7':
		nwone = (i + 1, j) if (i, j - 1) == last else (i, j - 1)
	elif elt == 'F':
		nwone = (i + 1, j) if (i, j + 1) == last else (i, j + 1)
	
	loopi.append(nwone)
	return nwone

startp = []
for i, nb in enumerate(nbl):
	if 'S' in nb:
		startp = (i, nb.index('S'))
		loopi.append(startp)
	fields.append(list(nb))

i = startp[0] 
j = startp[1]

#print(loopi[i + 1, j], loopi[i - 1, j], loopi[i, j - 1], loopi[i, j + 1])
if i + 1 < len(fields) and fields[i + 1][j] in ('|', 'J', 'L'):
	loopi.append((i + 1, j))
elif i - 1 > 0 and fields[i - 1][j] in ('|', 'F', '7'):
	loopi.append((i - 1, j))
elif j - 1 > 0 and fields[i][j - 1] in ('-', 'F', 'L'):
	loopi.append((i, j - 1))
elif j + 1 < len(fields[0]) and fields[i][j + 1] in ('-', 'J', '7'):
	loopi.append((i, j + 1))


while getNexit() != startp:
	continue


print((len(loopi) -1) / 2)