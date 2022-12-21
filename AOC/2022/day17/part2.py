from os import system
from time import sleep
nbl = open('data.txt').read()

total = 0
tetris = [['####'], ['.#.', '###', '.#.'], ['..#', '..#', '###'], ['#', '#', '#', '#'], ['##', '##']]
highr = 0
lvl = []
sizem = 7

def horizontal(curform, dire):
	forme = curform['forme']
	x = curform['x']
	y = curform['y']
	if dire == '>':
		for ilmn, lmn in enumerate(forme):
			maxr = x + len(lmn) if lmn[-1] == '#' else x + len(lmn) - 1
			if maxr >= sizem:
				return False
			elif lvl[y - ilmn][maxr] == '#':
				return False
		draw(curform, True)
		curform['x'] += 1
	elif dire == '<':
		for ilmn, lmn in enumerate(forme):
			if lmn[0] == '#':
				minr = x - 1
			elif lmn[1] == '#':
				minr = x	
			elif lmn[2] == '#':
				minr = x + 1	
			if minr < 0:
				return False
			elif lvl[y - ilmn][minr] == '#':
				return False
		draw(curform, True)
		curform['x'] -= 1
	return True

def goingdown(curform):
	global highr
	forme = curform['forme']
	x = curform['x']
	y = curform['y']
	draw(curform, True)

	if y - len(forme) < 0:
		highr = max(highr, y + len(forme))
		return False 
	for ix in range(len(forme[0])):
		ypos = len(forme) if forme[-1][ix] == '#' else len(forme) - 1
		if lvl[y - ypos][x + ix] == '#':
			highr = max(highr, y + 1)
			return False
	curform['y'] -= 1
	return True

index = -1
def draw(curform, clean):
	forme = curform['forme']
	x = curform['x']
	y = curform['y']
	for islide, slide in enumerate(forme):
		for ixx, xx in enumerate(slide):
			if clean and forme[islide][ixx] != '.':
				lvl[y - islide][x + ixx] = '.'
			elif lvl[y - islide][x + ixx] == '.':
				lvl[y - islide][x + ixx] = forme[islide][ixx]

def addup(curf):
	hg = 3 - (len(lvl) - highr - len(curf['forme']))
	if hg < 0:
		hg = 0
	for _ in range(hg):
		lvl.append(['.' for _ in range(7)])

gd = False
windi = 0
maxrok = 1000000000000
#maxrok = 2022
total = 1749
prev = 0
prevh = 0
prevh2 = 0
print((1000000000000 - 1749) / 1740 ) # -> 574712642
print((1000000000000 - 1749) - (574712642 * 1740)) # -> 1171
maxrok = 1749 + 1171 #  2920

while index < maxrok:
	if windi % len(nbl) == 0 and index >= 1:
		print(index, index - prev, highr, highr - prevh) # 1749 and 2716 redoundancy
		prev = index
		prevh = highr
	c = nbl[windi % len(nbl)]
	if gd == False:
		index += 1
		curform = {'forme': tetris[index % 5], 'y': 0, 'x': 2}
		dif = 3 - (len(lvl) - highr - len(curform['forme']))
		dif = 0 if dif > 0 else dif
		addup(curform)
		curform['y'] = len(lvl) - 1 + dif
	ho = horizontal(curform, c)
	gd = goingdown(curform)
	draw(curform, False)
	windi += 1
print('Part 2: {}'.format((574712642 * 2716) + highr))
