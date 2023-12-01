nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')
rep = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def isnumber(txt, revers):
	for k, v in rep.items():
		if len(k) <= len(txt):
			if(revers == 0 and k == txt[:len(k)]):
				return v
			elif(revers == 1 and k[::-1] == txt[:len(k)]):
				return v
	return False

def getfirst(txt, revers):
	for pos in range(len(txt)):
		if txt[pos].isdigit():
			return txt[pos]
		else:
			nbi = isnumber(txt[pos:], revers)
			if nbi:
				return nbi
	return False

total = 0
for nb in nbl:
	tmp = int(getfirst(nb, 0) + getfirst(nb[::-1], 1))
	total += tmp
print(total)