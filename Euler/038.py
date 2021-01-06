from utils import *


maxp = 0
def pandmul(nb):
	stri = ''
	for j in range(1, 9):
		stri += str(nb * j)
		if len(stri) > 9:
			return False
		elif len(stri) == 9 and is_pandigital(stri):
			return stri

for i in range(9999):
	pandi = pandmul(i)
	if pandi:
		print("Pandigital multiple: %s" % (i))
		maxp = max(maxp, pandi)
print("Max pandigital: %s" % (maxp))