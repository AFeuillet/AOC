nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

def ispossible(sent):
	games = sent.split(': ')[1].split('; ')
	for game in games:
		picks = game.split(', ')
		for pick in picks:
			p = pick.split(' ')
			if ((p[1] == 'red' and int(p[0]) > 12) or 
				(p[1] == 'green' and int(p[0]) > 13) or 
				(p[1] == 'blue' and int(p[0]) > 14)):
				return False
	return True

total = 0
counter = 1
for nb in nbl:
	if ispossible(nb):
		total += counter
	counter += 1
print(total)