import math
import re

nfile = open('data/day05.txt', 'r')
nbl = nfile.read().split('\n')
count = 0

def getSid(board):
	rmin = 0
	rmax = 127
	for letter in board[:-3]:
		rmid = float(rmax + rmin) / 2
		if letter == "F":
			rmax = int(math.floor(rmid))
		else:
			rmin = int(math.ceil(rmid))
	row = rmin
	rmin = 0
	rmax = 7	
	for letter in board[-3:]:
		rmid = float(rmax + rmin) / 2
		if letter == "R":
			rmin = int(math.ceil(rmid))
		else:
			rmax = int(math.floor(rmid))
	col = rmin
	return row * 8 + col 


fl = list(range(0, 935))
maxi = 0
for line in nbl:
	sid= getSid(line)
	maxi = max(sid, maxi)
	if sid in fl:
		fl.remove(sid)

print(maxi)
print(max(fl))