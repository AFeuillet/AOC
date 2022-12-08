signal = open('data.txt').read()

size = 14
for i in range(size, len(signal)):
	fourth = signal[i - size:i]
	found = True
	for j in range(1, size):
		if fourth.count(signal[i - j]) != 1:
			found = False
			break
	if found == True:
		print('Part 1: {}'.format(i))
		exit()