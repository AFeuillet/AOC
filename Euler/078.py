# Partition (number theory)
# p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)....
#  n -> (Pentagonal number)

maxi = 1000000

pentag = []
for i in range(1, maxi):
	pentag.append(int((i * ((3 * i) - 1)) / 2))
	pentag.append(int((-i * ((3 * -i) - 1)) / 2))

p = {}
p[0] = 1
p[1] = 1
for i in range(1, maxi):
	p[i] = 0
	j = 0
	ch = 0
	while i - pentag[j] >= 0:
		if ch < 2:
			p[i] += p[i - pentag[j]]
		else:
			p[i] -= p[i - pentag[j]]
		ch += 1
		if ch >= 4:
			ch = 0
		j += 1
	if p[i] % 1000000 == 0:
		print("Found:", i)
		exit()