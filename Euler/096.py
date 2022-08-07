import copy
from utils import *


def display_sudok(sudok):
	i = 0
	j = 0
	for line in sudok:
		for ll in line:
			if not isinstance(ll, int) and len(ll) == 1:
				print(ll[0], end ='')
			else:
				print(ll, end ='')
			j += 1 
			if j == 3:
				print(' | ', end ='')
				j = 0
			else:
				print(', ', end ='')
		print()
		i += 1 
		if i == 3:
			print()
			i = 0
	print('----------------------')


def check_resolved(sudok):
	for line in sudok:
		for val in line:
			if len(val) > 1:
				return False
	return True


def check_alone(sudok, m, n, a):
	findo = -1
	for i in range(3):
		for j in range(3):
			if len(sudok[i + (m * 3)][j + (n * 3)]) == 1:
				if sudok[i + (m * 3)][j + (n * 3)][0] == a:
					return True
				else:
					continue
			elif a in sudok[i + (m * 3)][j + (n * 3)]:
				if findo == -1:
					findo = [i, j]
				else:
					return False
	if findo != -1:
		sudok[findo[0] + (m * 3)][findo[1] + (n * 3)] = [a]
		return True
	else:
		return False

#First method using tactics only work half a time 
def solve(sudok):
	tempmax = 10
	t = 0
	while(t < tempmax and check_resolved(sudok) == False):
		for i in range(9):
			for j in range(9):
				if len(sudok[i][j]) == 1:
					d = sudok[i][j][0]
					for l in range(9):
						if l != i and d in sudok[l][j]:
							sudok[l][j].remove(d)
					for l in range(9):
						if l != j and d in sudok[i][l]:
							sudok[i][l].remove(d)
		
		for m in range(3):
			for n in range(3):
				for a in range(1, 10):
					check_alone(sudok, m, n, a)
				for i in range(3):
					for j in range(3):
						if len(sudok[i + (m * 3)][j + (n * 3)]) == 1:
							d = sudok[i + (m * 3)][j + (n * 3)][0]
							for ia in range(3):
								for ja in range(3):
									if i == ia and j == ja:
										continue
									if  d in sudok[ia + (m * 3)][ja + (n * 3)]:
										sudok[ia + (m * 3)][ja + (n * 3)].remove(d)	
		t += 1
	
	display_sudok(sudok)
	if t == tempmax:
		return False
	return True

def checksudo(sudok, i, j, n):
	for v in range(9):
		if sudok[i][v] == n:
			return False
		if sudok[v][j] == n:
			return False
	x = (i // 3) * 3
	y = (j // 3) * 3
	for a in range(3):
		for b in range(3):
			if sudok[x + a][y + b] == n:
				return False
	return True

#Recursive Method
thr = ''
def solve_iter(sudok):
	global thr
	for i in range(9):
		for j in range(9):			
			if sudok[i][j] == 0:
				for n in range(1, 10):
					if checksudo(sudok, i, j, n):
						sudok[i][j] = n
						solve_iter(sudok)
						sudok[i][j] = 0
				return
	display_sudok(sudok)
	thr = '%s%s%s' % (sudok[0][0], sudok[0][1], sudok[0][2] )

i = -1 
s = []
tentative = 0
total = 0
for line in load_data('096'):
	if i == -1:
		i += 1
		sudok = [
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],

			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],

			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
			[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ]
		]
		sudok2 = copy.deepcopy(sudok)
		continue

	
	for j in range(9):
		sudok2[i][j] = int(line[j])
		if int(line[j]) != 0:
			sudok[i][j] = [int(line[j])]
		else:
			sudok[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	i += 1
	if i == 9:
		#if solve(sudok) == False:
		#	tentative += 1
		 
		solve_iter(sudok2)
		print(thr)
		total += int(thr)
		i = -1


print("Total:", total)
