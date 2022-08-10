import math
maxi = 10001
maxcyc = 500
S = {}
nbodd = 0

def getperiod(seq):
	findp = True
	maxsize = 250
	for j in range(1, maxsize):
		found = True
		firs = seq[0:j]
		i = 0
		while found and len(seq) > (i + j):
			if firs != seq[i:i + j]:
				found = False
			i += j
		if found:
			return firs
	return [-1]

def getfraction(i, sq):
	global nbodd
	first = int(sq)
	seq = []
	period = 0
	a = 1
	b = first
	for i in range(maxcyc):
		# a / sq - b 
		# a (sq + b) / (sq - b) * (sq + b)
		c = round((sq - b) * (sq + b))

		# d + (sq - b) / a
		a = int(c / a)
		d = int((sq + b) / a)
		b = - (b - (d * a))
		seq.append(d)
	periodlen = len(getperiod(seq))
	if periodlen % 2 != 0:
		nbodd += 1
	return [first, seq, periodlen]

for i in range(2, maxi):
	sq = math.sqrt(i)
	if not sq.is_integer():
		S[i] = getfraction(i, sq)

print(nbodd)