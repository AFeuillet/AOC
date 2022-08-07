from itertools import combinations

def isin(a, b, ap, bp):
	a = str(a)
	b = str(b)
	if (a in ap and b in bp) or (a in bp and b in ap):
		return True
	return False

def isinsix(a, ap, bp):
	a = str(a)
	if (a in ap and ('6' in bp or '9' in bp)) or (a in bp and ('6' in ap or '9' in ap)):
		return True
	return False

def digitp(a, b):
	if a == b:
		return False
	astr = ''.join(sorted(a))
	bstr = ''.join(sorted(b))
	if astr == bstr:
		return False
	if astr + bstr in diceset or bstr + astr in diceset:
		return False
	easycub = [(0, 1), (0, 4), (2, 5), (8, 1)]
	for ec in easycub:
		if isin(ec[0], ec[1], astr, bstr) == False:
			return False
	spcubs = [0, 1, 3, 4]
	for sp in spcubs:
		if isinsix(sp, astr, bstr) == False:
			return False

	diceset.add(astr + bstr)
	return True
	

diceset = set()
per = list(combinations('0123456789', 6))
for i in per:
	for j in per:
		digitp(i, j)

print(len(diceset))