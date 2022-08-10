from utils import *

graphi = [
	[131, 673, 234, 103,18],
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331]]


graphi = []
for line in load_data('082'):
	graphi.append([int(a) for a in line.split(',')])

shorter = 999999
"""
# First method reccuring: Too Long
def goto(i, j, direc, som):
    global shorter
    som += graph[i][j]
    if som > shorter:
        return
    if j == len(graph[0]) - 1:
        if som < shorter:
            shorter = som
        return
    if direc in [-1, 0] and i - 1 >= 0:
        goto(i - 1, j, direc, som)
    if direc in [0, 1] and i + 1 < len(graph):
        goto(i + 1, j, direc, som)
    goto(i, j + 1, 0, som)

for i in range(len(graph)):
    goto(i, 0, 0, 0)
"""

# Second method compute by the end row by row
def computrow(graphi, row):
    siz = len(graphi)
    for i in range(siz):
        maxi = graphi[i][row] + graphi[i][row + 1]
        tmp = 0
        # bottom
        for j in range(i, siz):
            tmp += graphi[j][row]
            if maxi >= tmp + graphi[j][row + 1]:
                maxi = tmp + graphi[j][row + 1]
            else:
                break
        # top
        if i > 0 and maxi > graphi[i][row] + graphi[i - 1][row]:
            maxi = graphi[i][row] + graphi[i - 1][row]
        graphi[i][row] = maxi


for i in range(len(graphi) - 2, -1, -1):
    computrow(graphi, i)

for i in range(len(graphi)):
    if graphi[i][0] < shorter:
        shorter = graphi[i][0]

print(shorter)