nfile = open('data/day11.txt', 'r')
nbl = nfile.read().split('\n')

octopus = []
maxsteps = 1000
total = []
total.append(0)

for line in nbl:
	octopus.append([int(a) for a in line])

def printIt(step, octopus):
	print('step %s:' % (step + 1))
	for i in range(len(octopus)):
		for j in range(len(octopus[i])):
			if octopus[i][j] == 0:
				print('\033[1m%s\033[0m' % octopus[i][j],  end ='')
			else:
				print('%s' % octopus[i][j],  end ='')
		print()
	print()

def popIt(i ,j, state):
	if state == 1 and octopus[i][j] < 10 and octopus[i][j] > 0:
		octopus[i][j] += 1
	if octopus[i][j] == 10:
		octopus[i][j] = 0
		total[0] += 1 
		if i - 1 >= 0:
			if j - 1 >= 0:
				popIt(i - 1, j - 1, 1)
			if j + 1 < len(octopus):
				popIt(i - 1, j + 1, 1)
			popIt(i - 1, j, 1)
		if i + 1 < len(octopus):
			if j - 1 >= 0:
				popIt(i + 1, j - 1, 1)
			if j + 1 < len(octopus):
				popIt(i + 1, j + 1, 1)
			popIt(i + 1, j, 1)
		if j - 1 >= 0:
			popIt(i, j - 1, 1)
		if j + 1 < len(octopus):
			popIt(i, j + 1, 1)

def blink(octopus):
	for i in range(len(octopus)):
		for j in range(len(octopus[i])):
			if octopus[i][j] != 0:
				return False
	return True

printIt(0, octopus)
for step in range(maxsteps):
	for i in range(len(octopus)):
		for j in range(len(octopus[i])):
			octopus[i][j] += 1
	for i in range(len(octopus)):
		for j in range(len(octopus[i])):
			popIt(i, j, 0)	
	printIt(step, octopus)
	if step == 100:
		print("Part One: %s" % total)
	if blink(octopus):
		print("Part Two: %s" % (step + 1))
		exit()