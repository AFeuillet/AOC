nfile = open('data/day08.txt', 'r')
nbl = nfile.read().split('\n')

pos = 0
acc = 0
run = []

# filling the run
for line in nbl:
	(op, val) = line.split(" ")
	run.append([op, val, 0]) 

while True:
	if run[pos][0] == 'acc':
		acc += int(run[pos][1])
		pos += 1
	elif run[pos][0] == 'nop':
		pos += 1
	elif run[pos][0] == 'jmp':
		pos += int(run[pos][1])
	if run[pos][2] == 1:
		break
	run[pos][2] = 1
	
print(acc)