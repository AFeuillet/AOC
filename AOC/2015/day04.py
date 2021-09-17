import hashlib

nfile = open('data/day04.txt', 'r')
key = nfile.read()
maxi = 99999999
for i in range(maxi):
	hashg = hashlib.md5(bytes('%s%s' % (key, i), 'utf-8')).hexdigest()
	if hashg[:5] == '00000':
		print("Part One: %s" % i)
		break

for i in range(maxi):
	hashg = hashlib.md5(bytes('%s%s' % (key, i), 'utf-8')).hexdigest()
	if hashg[:6] == '000000':
		print("Part Two: %s" % i)
		break