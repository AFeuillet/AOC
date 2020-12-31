from utils import *


maxd = 28123
total = 0
abundants = []
for i in range(maxd):
	if proper_sum(i) > i:
		abundants.append(i)

def is_sumabunds(value):
	for j in abundants:
		for k in abundants:
			if j + k == value:
				return True
			elif j + k > value:
				break
		if j > value:
			return False
	return False

for i in range(maxd):
	if is_sumabunds(i) == False:
		total += i

print(total)