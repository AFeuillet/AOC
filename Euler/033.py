total = 1
def divide(a, b):
	print('%s / %s ' % (a, b))
	if a > b:
		return a / float(b)
	else:		
		return b / float(a)

for i in range(10, 100):
	for j in range(i + 1, 100):
		di = i / 10
		dj = j / 10
		ui = i % 10
		uj = j % 10
		if uj != 0 and di == dj and ui / float(uj) == i / float(j):
			total *= divide(i, j)
		elif di == uj and ui / float(dj) == i / float(j):
			total *= divide(i, j)
		elif uj != 0 and ui == dj and di / float(uj) == i / float(j):
			total *= divide(i, j)
		elif uj != 0 and ui == uj and di / float(dj) == i / float(j):
			total *= divide(i, j)
print(total)