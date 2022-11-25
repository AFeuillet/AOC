from itertools import permutations
"""
 tabi = 1,2,3

  4
   \
    3
   / \
  1 - 2 - 6
 /
5

# 16 digit str -> 10 is on the external
"""

size = 5

listbase = list(range(1, size * 2 +1))
combl = list(permutations(listbase, size))
#print(combl)
print(len(combl))

def poscong(tab, sub, size):
	if size == 3 and tab[0] + tab[1] + sub[0] ==  tab[1] + tab[2] + sub[1] == tab[2] + tab[0] + sub[2]:
		p = [sub[0], tab[1], tab[0], sub[2], tab[0], tab[2], sub[1], tab[2], tab[1]]
		ind = p.index(min(p[0 * 3], p[1 * 3], p[2 * 3]))
		return(p[ind:] + p[:ind])
	if size == 5 and tab[0] + tab[1] + sub[0] ==  tab[1] + tab[2] + sub[1] == tab[2] + tab[3] + sub[2] == tab[3] + tab[4] + sub[3] == tab[4] + tab[0] + sub[4]:
		p = [sub[0], tab[1], tab[0], sub[4], tab[0], tab[4], sub[3], tab[4], tab[3], sub[2], tab[3], tab[2], sub[1], tab[2], tab[1]]
		ind = p.index(min(p[0 * 3], p[1 * 3], p[2 * 3], p[3 * 3], p[4 * 3]))
		return(p[ind:] + p[:ind])
	return False

def findcong(tab):
	if 10 in tab:
		return False
	sub = [x for x in listbase if x not in tab]
	for perm in list(permutations(sub, size)):
		pc = poscong(tab, perm, size)
		if pc:
			print(pc, sum(pc[0:size]))
			return pc
	return False

maxi = 0
for combi in combl:
	fd = findcong(combi)
	if fd is not False:
		maxi = max(maxi, int(''.join(map(str, fd))))
print(maxi)