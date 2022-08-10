from random import random

plateau = [0] * 40
nbcoup = 5000000
triple = 0
pos = 0
chpos = 0
copos = 0

def rolldice():
	return [int(random() * 4) + 1, int(random() * 4) + 1]

def chanc(pos):
	global chpos
	if chpos < 6:
		pos = [0, 10, 11, 24, 39, 5][chpos] 
	elif chpos in [6, 7]:
		if pos < 5:
			pos = 5
		elif pos < 15:
			pos = 15
		elif pos < 25:
			pos = 25
		else:
			pos = 35
	elif chpos == 8:
		if pos < 12:
			pos = 12
		else:
			pos = 27
	elif chpos == 9:
		pos -= 3
	chpos += 1	
	if chpos >= 16:
		chpos = 0
	return pos

def commu(pos):
	global copos
	if copos < 2:
		pos = [0, 10][copos]
	copos += 1
	if copos >= 16:
		copos = 0
	return pos


for i in range(nbcoup):
	dice = rolldice()
	pos += (dice[0] + dice[1])
	pos = pos % 40
	if dice[0] == dice[1]:
		triple += 1
	if triple == 3:
		pos = 10

	# Dirct to prison
	if pos == 30:
		pos = 10

	# Chance
	if pos in [7, 22 ,36]:
		pos = chanc(pos)

	# Commmunauty
	if pos in [2, 17 ,33]:
		pos = commu(pos)

	plateau[pos] += 1

print(plateau)
print(sorted(zip(plateau, range(40) ), reverse=True)[:3])