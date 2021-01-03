nfile = open('data/day14.txt', 'r')
nbl = nfile.read().split('\n')

mask = 'o'
total = 0
memo = {}

for line in nbl:
	li = line.replace(' ','').split('=')
	if li[0] == 'mask':
		mask = li[1]
		continue
	else:
		byts = '{0:b}'.format(int(li[1]))
		fullbyts = list('0' * (len(mask) - len(byts)) + byts)

		for i in range(len(mask)):
			if mask[i] != 'X':
				fullbyts[i] = mask[i]
		newvalue = ''.join(fullbyts)
		memo[li[0][4:-1]] = int(newvalue, 2)
for k,v in memo.items():
	total += int(v)
print(total)