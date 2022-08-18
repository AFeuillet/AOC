from utils import *
"""
3 7 109 673
"""
def is_pp2(p1, p2):
	return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))

sprimes = all_primes(9999)
S = {}
for i in range(len(sprimes)):
	for j in range(i, len(sprimes)):
		if is_pp2(sprimes[i], sprimes[j]):
			if sprimes[i] not in S:
				S[sprimes[i]] = set()
			S[sprimes[i]].add(sprimes[j])
			if sprimes[j] not in S:
				S[sprimes[j]] = set()
			S[sprimes[j]].add(sprimes[i])

minv = 9999999
for sv0 in S.items():
	tabi = [sv0[0]]
	for a in sv0[1]:
		if a not in S:
			break
		elif tabi[0] not in S[a]:
			break
		else:
			tabi.append(a)
			for b in S[a]:
				pot = True
				for t in tabi:
					if t not in S[b]:
						pot = False
				if pot == False:
					break
				else:
					tabi.append(b)
					for bp in S[b]:
						pot = True
						for t in tabi:
							if t not in S[bp]:
								pot = False
						if pot == True:
							tabi.append(bp)
							for c in S[bp]:
								pot = True
								for t in tabi:
									if t not in S[c]:
										pot = False
								if pot == True:
									tabi.append(c)
									total = 0
									for i in tabi:
										total += i
									if total < minv:
										minv = total
									break
							tabi.pop()
					tabi.pop()
			tabi.pop()
print(minv)	
