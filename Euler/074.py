import math

loopi = {}
facti = {}

def factval(val):
	total = 0
	for j in str(val):
		total += math.factorial(int(j))
	return total
	
for i in range(1000000):
	curloop = [i]
	curi = i
	while True:
		if curi not in facti:
			facti[curi] = factval(curi)
		if facti[curi] in curloop:
			loopi[i] = len(curloop)
			break
		elif facti[curi] in loopi:
			loopi[i] = len(curloop) + loopi[facti[curi]]
			break
		curloop.append(facti[curi])
		curi = facti[curi]
maxc = max(list(loopi.values()))
print('Max chain :', maxc)
print('Number of mx :', list(loopi.values()).count(maxc))
