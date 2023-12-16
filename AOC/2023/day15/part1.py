nfile = open('data.txt', 'r')
nbl = nfile.read().replace('\n', '').split(',')

def getValue(txt):
	curval = 0
	for c in txt:
		curval += ord(c)
		curval *= 17
		curval %= 256
	return curval

total = 0
for nb in nbl:
	total += getValue(nb)
print(total)