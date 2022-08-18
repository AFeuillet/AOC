from utils import *
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.
"""

S = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
tab = []
for line in load_data('089'):
	total = 0
	lline = len(line)
	for i in range(lline):
		ch = line[i]
		if i + 1 < lline and (
			(ch == 'I' and (line[i + 1] == 'V' or line[i + 1] == 'X')) or 
			(ch == 'X' and (line[i + 1] == 'L' or line[i + 1] == 'C')) or 
			(ch == 'C' and (line[i + 1] == 'D' or line[i + 1] == 'M'))):
			total -= S[ch]
		else:
			total += S[ch]
	tab.append((line, lline, total))

ntab = []
total = 0
for rom in tab:
	nb = rom[2]
	nbc = ''
	if nb // 1000 != 0:
		nbc += (nb // 1000) * 'M'
	if (nb // 100) % 10 != 0:
		a = (nb // 100) % 10
		if a == 9:
			nbc += 'CM'
		elif a >= 5:
			nbc += 'D' + (a - 5) * 'C'
		elif a == 4:
			nbc += 'CD'
		else:
			nbc += 'C' * a
	if (nb // 10) % 10 != 0:
		a = (nb // 10) % 10
		if a == 9:
			nbc += 'XC'
		elif a >= 5:
			nbc += 'L' + (a - 5) * 'X'
		elif a == 4:
			nbc += 'XL'
		else:
			nbc += 'X' * a
	if nb % 10 != 0:
		a = nb % 10
		if a == 9:
			nbc += 'IX'
		elif a >= 5:
			nbc += 'V' + (a - 5) * 'I'
		elif a == 4:
			nbc += 'IV'
		else:
			nbc += 'I' * a
	total += rom[1] - len(nbc)
	ntab.append((rom[0], nbc, rom[1] - len(nbc)))

for n in ntab:
	print(n)
print(total)
