import math
nbl = open('data.txt').read().split('\n')

maxscenic = 0
forest = []
scenic = []

def display(matrix):
	for m in matrix:
		print(m)
	print()

for line in nbl:
	forest.append([int(i) for i in line])
	scenic.append([0 for i in line])

for i in range(1, len(forest[0]) - 1):
	for j in range(1, len(forest[i]) - 1):
		tree = forest[i][j]
		lrtb = [0, 0, 0, 0]
		# Left
		for k in range(j - 1, -1, -1):
			lrtb[0] += 1
			if tree <= forest[i][k]:
				break
		# Right
		for k in range(j + 1, len(forest[i]), 1):
			lrtb[1] += 1
			if tree <= forest[i][k]:
				break
		# Top
		for k in range(i - 1, -1, -1):
			lrtb[2] += 1
			if tree <= forest[k][j]:
				break
		# Bottom
		for k in range(i + 1, len(forest[0]), 1):
			lrtb[3] += 1
			if tree <= forest[k][j]:
				break

		scenic[i][j] = math.prod(lrtb)
		maxscenic = max(scenic[i][j], maxscenic)

display(scenic)
print('Part 2: {}'.format(maxscenic))