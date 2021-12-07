nfile = open('data/day02.txt', 'r')
nbl = nfile.read().split('\n')

def dayTwoa():
	horiz = 0
	depth = 0
	for line in nbl:
		action, n = line.split(' ')
		ni = int(n)
		if action == 'forward':
			horiz += ni
		elif action  == 'down':
			depth += ni
		elif action == 'up':
			depth -= ni
	return horiz * depth


def dayTwob():
	horiz = 0
	depth = 0
	aim = 0
	for line in nbl:
		action, n = line.split(' ')
		ni = int(n)
		if action == 'forward':
			horiz += ni
			depth += aim * ni
		elif action  == 'down':
			aim += ni
		elif action == 'up':
			aim -= ni
	return horiz * depth

#print(dayTwoa())
print(dayTwob())