maxi = 100
e = [2, 3]
multiplier = 0
c = 0
# numerator as relation together
for i in range(2, maxi):
	if c == 0:
		multiplier += 2
		d = multiplier
	else:
		d = 1
	e.append((d * e[i - 1]) + e[i - 2])
	c += 1
	if c > 2:
		c = 0

total = 0
for ch in str(e[99]):
	total += int(ch)

print(total)