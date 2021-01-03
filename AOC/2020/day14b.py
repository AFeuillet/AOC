import copy


nfile = open('data/day14.txt', 'r')
nbl = nfile.read().split('\n')

mask = 'o'
total = 0
memo = {}
submemo = []

def initx(fb, pos, value):
	fb[pos] = value
	sumb = copy.deepcopy(fb)
	for i in range(pos + 1, len(mask)):
		if mask[i] == 'X':
			initx(sumb, i, '0')
			initx(sumb, i, '1')
	submemo.append(sumb)

for line in nbl:
	li = line.replace(' ','').split('=')
	if li[0] == 'mask':
		mask = li[1]
		continue
	else:
		byts = '{0:b}'.format(int(li[0][4:-1]))
		fullbyts = list('0' * (len(mask) - len(byts)) + byts)
		value = int(li[1])
		submemo = []
		for i in range(len(mask)):
			if mask[i] == '1':
				fullbyts[i] = '1'
		if 'X' not in mask:
			memo[int(''.join(fullbyts), 2)] = value
		else:	
			for i in range(len(mask)):
				if mask[i] == 'X':
					initx(fullbyts, i, '0')
					initx(fullbyts, i, '1')
			for subm in submemo:
				memo[int(''.join(subm), 2)] = value
		
for k,v in memo.items():
	total += int(v)
print(total)