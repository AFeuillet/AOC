from utils import *

linenb = 1
biggerline = 1
biggernb = [1, 1]
for line in load_data('099'):
	nb = line.split(',')
	if  (biggernb[0] <= int(nb[0]) or biggernb[1] <= int(nb[1])) and (int(nb[0]) ** int(nb[1]) > biggernb[0] ** biggernb[1]):
		biggerline = linenb
		biggernb = [int(nb[0]), int(nb[1])]
	linenb += 1
print(biggerline)