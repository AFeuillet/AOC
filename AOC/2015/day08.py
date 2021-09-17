import re

nfile = open('data/day08.txt', 'r')
nbl = nfile.read().split('\n')


total = 0
for word in nbl:
	nbcar = len(word)
	cleaned = word.replace('\\\\', 'Y').replace('\\"', 'X').replace('"', '')
	cleaned = re.sub(r"\\x..", "Z", cleaned)
	total += len(word) - len(cleaned)
print("Part One: %s" % total)


total = 0
for word in nbl:
	nbcar = len(word)
	encoded = word.replace('\\\\', 'YYYY').replace('\\"', 'AAAA').replace('"', 'XXX')
	encoded = re.sub(r"\\x..", "ZZZZZ", encoded)
	total += len(encoded) - len(word)
print("Part Two: %s" % total)