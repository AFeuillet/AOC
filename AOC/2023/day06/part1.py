import re

nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

times = [int(n) for n in re.findall(r'(\d+)', nbl[0])]
records = [int(n) for n in re.findall(r'(\d+)', nbl[1])]

total = 0
bigtotal = 1
for k, tim in enumerate(times):
	status = False
	total = 0
	for trry in range(records[k]):
		if (tim * trry - trry ** 2) > records[k]:
			status = True
			total += 1
		elif status == True:
			bigtotal *= total
			break

print(bigtotal)