from utils import *


maxnb = 2000
total = 0
totalset = set()
for i in range(1, maxnb):
    for j in range(1, maxnb):
    	multi = i * j
        val  = str(i) + str(j) + str(multi)
        if len(val) == 9 and is_pandigital(val):
            print ("%s * %s = %s , %s" % (i, j, multi, val) )
            totalset.add(multi)
print(sum(totalset))
