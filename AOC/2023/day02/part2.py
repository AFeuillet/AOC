nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

def spower(sent):
	games = sent.split(': ')[1].split('; ')
	mincol = {'red': 0, 'green': 0, 'blue': 0}
	for game in games:
		picks = game.split(', ')
		for pick in picks:
			p = pick.split(' ')
			mincol[p[1]] = max(mincol[p[1]], int(p[0]))
	return mincol['red'] * mincol['green'] * mincol['blue']

total = 0
for nb in nbl:
	total += spower(nb)

print(total)