nbl = open('data.txt').read().split('\n')

cycle = 0
x = 1

CRT = []
def checkloop(cycle, x):
	global CRT
	pos = (cycle - 1) % 40
	if pos >= x - 1 and pos <= x + 1:
		CRT.append('#')
	else:
		CRT.append('.')

for iline, line  in enumerate(nbl):
	cycle += 1
	checkloop(cycle, x)
	if line != 'noop':
		cycle += 1
		checkloop(cycle, x)
		instr, value = line.split(' ')
		x += int(value)

for i in range(6):
	for j in CRT[i * 40:(i + 1) * 40]:
		print(j + ' ', end = '')
	print()
