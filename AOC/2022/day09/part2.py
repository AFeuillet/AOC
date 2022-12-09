from os import system
from time import sleep

nbl = open('data.txt').read().split('\n')

paths = {}
head = [0, 0]
#tail = [0, 0]

sizeof = [0, 0, 0, 0]
def displays(head):
	system('clear')
	xdecal = abs(sizeof[0])
	xsiz = sizeof[1] + xdecal + 1
	ydecal = abs(sizeof[2])
	ysiz = sizeof[3] + ydecal + 1
	tot = [['.' for j in range(xsiz)] for i in range(ysiz)] 

	if len(tot) == 0:
		return
	for p in paths.items():
		tot[p[0][1] + ydecal][p[0][0] + xdecal] = '#'
	tot[head[1] + ydecal][head[0] + xdecal] = 'T'
	tot[ydecal][xdecal] = 'S'
	tot.reverse()
	for i in range(ysiz):
		for j in tot[i]:
			print(j, end ='')
		print()
	#sleep(0.1)

tails = [[0, 0]for i in range(9)]
for iline, line  in enumerate(nbl):
	mov, dis = line.split(' ')
	
	for i in range(0, int(dis)):
		if mov == 'R':
			head[0] += 1
		elif mov == 'L':
			head[0] -= 1
		elif mov == 'U':
			head[1] += 1
		elif mov == 'D':
			head[1] -= 1

		xbase = head[0]
		ybase = head[1]

		ti = 0
		for ti in range(9):
			x = xbase - tails[ti][0]
			y = ybase - tails[ti][1]

			if x > 1:
				tails[ti][0] += 1
				if y > 0:
					tails[ti][1] += 1
				elif y < 0:
					tails[ti][1] -= 1
			elif x < -1:
				tails[ti][0] -= 1
				if y > 0:
					tails[ti][1] += 1
				elif y < 0:
					tails[ti][1] -= 1
			elif y > 1:
				tails[ti][1] += 1
				if x > 0:
					tails[ti][0] += 1
				elif x < 0:
					tails[ti][0] -= 1
			elif y < -1:
				tails[ti][1] -= 1
				if x > 0:
					tails[ti][0] += 1
				elif x < 0:
					tails[ti][0] -= 1
			xbase = tails[ti][0]
			ybase = tails[ti][1]

		paths[(tails[8][0], tails[8][1])] = 1
		# for display
		sizeof = [min([head[0], sizeof[0]]), max([head[0], sizeof[1]]), min([head[1], sizeof[2]]), max([head[1], sizeof[3]])]
		#displays(head)

print('Part 2: {}'.format(len(paths)))
