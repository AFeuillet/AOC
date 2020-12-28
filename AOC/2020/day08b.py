nfile = open('data/day08.txt', 'r')
nbl = nfile.read().split('\n')


run = []

# filling the run
for line in nbl:
	(op, val) = line.split(" ")
	run.append([op, val, 0, 0]) 


def loopi(val):
	gc = False
	pos = 0
	acc = 0
	while True:
		if run[pos][3] == 1:
			if run[pos][0] == 'nop':
				run[pos][0] = 'jmp'
				run[pos][3] = 2
			elif run[pos][0] == 'jmp':
				run[pos][0] = 'nop'
				run[pos][3] = 2
		if gc == False and run[pos][3] == 0:
			if run[pos][0] == 'nop':
				run[pos][0] = 'jmp'
				run[pos][3] = 1
				gc = True
			elif run[pos][0] == 'jmp':
				run[pos][0] = 'nop'
				run[pos][3] = 1
				gc = True

		if run[pos][0] == 'acc':
			acc += int(run[pos][1])
			pos += 1
		elif run[pos][0] == 'nop':
			pos += 1
		elif run[pos][0] == 'jmp':
			pos += int(run[pos][1])
		if pos +1 > len(run) or run[pos][2] == val:
			break
		run[pos][2] = val

	if pos +1 > len(run):
		return acc
	else:
		return True

n = 0
whili = True
while whili == True:
	whili = loopi(n)
	n += 1

print(whili)