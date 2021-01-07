from itertools import permutations


maxperm = '0123456789'
allperms = permutations(maxperm, 10)

def spepanda(n):
	if (int(n[1]+n[2]+n[3]) % 2 == 0 and 
		int(n[2]+n[3]+n[4]) % 3 == 0 and 
		int(n[3]+n[4]+n[5]) % 5 == 0 and
		int(n[4]+n[5]+n[6]) % 7 == 0 and
		int(n[5]+n[6]+n[7]) % 11 == 0 and
		int(n[6]+n[7]+n[8]) % 13 == 0 and
		int(n[7]+n[8]+n[9]) % 17 == 0):
		return True
	return False

total = 0
for perm in allperms:
	if spepanda(perm):
		permi = int(''.join(perm))
		total += permi
		print("Special pandigital: %s" % (permi))
print("Sum special pandigital: %s" % (total))