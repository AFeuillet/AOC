nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

rocks = []

def goUp():
	for i in range(len(rocks) - 1):
		for j in range(len(rocks[0])):
			if rocks[i][j] == '.' and rocks[i + 1][j] == 'O':
				rocks[i][j] = 'O'
				rocks[i + 1][j] = '.'
for nb in nbl:
	rocks.append(list(nb))
for k in range(len(rocks) - 1):
	goUp()

total = 0
for i in range(len(rocks)):
	total += rocks[i].count('O') * (len(rocks) - i)
print(total)