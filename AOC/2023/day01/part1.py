nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

def getfirst(txt):
	for c in txt:
		if c.isdigit():
			return c
	return False

total = 0
for nb in nbl:
	total += int(getfirst(nb) + getfirst(nb[::-1]))

print(total)