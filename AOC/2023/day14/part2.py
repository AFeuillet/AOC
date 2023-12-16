nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

rocks = []

def goNorth():
	for k in range(len(rocks) - 1):
		for i in range(len(rocks) - 1):
			for j in range(len(rocks[0])):
				if rocks[i][j] == '.' and rocks[i + 1][j] == 'O':
					rocks[i][j] = 'O'
					rocks[i + 1][j] = '.'

def goSouth():
	for k in range(len(rocks) - 1):
		for i in range(len(rocks) - 1):
			for j in range(len(rocks[0])):
				if rocks[i + 1][j] == '.' and rocks[i][j] == 'O':
					rocks[i][j] = '.'
					rocks[i + 1][j] = 'O'

def goEast():
	for k in range(len(rocks[0]) - 1):
		for i in range(len(rocks)):
			for j in range(len(rocks[0]) - 1):
				if rocks[i][j + 1] == '.' and rocks[i][j] == 'O':
					rocks[i][j + 1] = 'O'
					rocks[i][j] = '.'

def goWest():
	for k in range(len(rocks[0]) - 1):
		for i in range(len(rocks)):
			for j in range(len(rocks[0]) - 1):
				if rocks[i][j] == '.' and rocks[i][j + 1] == 'O':
					rocks[i][j + 1] = '.'
					rocks[i][j] = 'O'
for nb in nbl:
	rocks.append(list(nb))

for op in range(500):
	goNorth()
	goWest()
	goSouth()
	goEast()
	total = 0
	for i in range(len(rocks)):
		total += rocks[i].count('O') * (len(rocks) - i)
	print(op, total)

for r in rocks:
	print(r)

"""
121 96097
122 96095
123 96093
124 96096
125 96112
126 96132
127 96141
128 96141
129 96124
130 96105
131 96094
132 96097
133 96095
134 96093
135 96096
136 96112
137 96132
138 96141
139 96141
140 96124
141 96105
"""
