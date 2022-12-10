nbl = open('data.txt').read().split('\n')

cycle = 0
x = 1
total = 0
def checkloop(cycle, x):
	global total
	if cycle in [20, 60, 100, 140, 180, 220]:
		total += cycle * x

for iline, line  in enumerate(nbl):
	cycle += 1
	checkloop(cycle, x)
	if line != 'noop':
		cycle += 1
		checkloop(cycle, x)
		instr, value = line.split(' ')
		x += int(value)

print('Part 1: {}'.format(total))