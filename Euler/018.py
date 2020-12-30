from utils import *

triangle =[]
for line in load_data('018'):
	triangle.append(list(map(int, line.split(' '))))

for i in range(len(triangle) - 2, -1, -1):
	for j in range(len(triangle[i])):
		triangle[i][j] = max(triangle[i][j] + triangle[i + 1][j], triangle[i][j] + triangle[i + 1][j + 1])
print(triangle[0][0])