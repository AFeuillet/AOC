goal = 2000000
n = 0
aire = 0
for i in range(1, int(goal / 2)):
	for j in range(1, int(goal / 2)):
		g = ((i * (i + 1)) / 2) * ((j * (j + 1)) / 2)
		if abs(goal - g) < abs(goal - n):
			aire = i * j
			n = g
		if g > goal:
			break

print(n)
print(aire)