nfile = open('data/day10.txt', 'r')
nbl = nfile.read().split('\n')
nbi = [int(a) for a in nbl]

alrs = {0: 1}
for adapt in sorted(nbi):
	alrs[adapt] = 0
	if adapt - 1 in alrs:
		alrs[adapt] += alrs[adapt - 1]
	if adapt - 2 in alrs:
		alrs[adapt] += alrs[adapt - 2]
	if adapt - 3 in alrs:
		alrs[adapt] += alrs[adapt - 3]
print(alrs)