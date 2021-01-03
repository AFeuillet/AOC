nfile = open('data/day16.txt', 'r')
nbl = nfile.read().split('\n\n')
rulines = nbl[0].split('\n')
rules = []
for line in rulines:
	a = line.split(': ')
	b = a[1].split(' or ')
	rules.append(b[0])
	rules.append(b[1])

rulines = nbl[2].split('\n')
def inthat(chk):
	for rule in rules:
		(amin, amax) = rule.split('-')
		if chk >= int(amin) and chk <= int(amax):
			return True
	return False

total = 0
rulines.pop(0)
for line in rulines:
	chks = line.split(',')
	for chk in chks:
		if not inthat(int(chk)):
			total += int(chk)

print(total)