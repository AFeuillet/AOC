maxi =  10000000
total = 0
S = {}

def maquethmsq(val):
	if val in S:
		return S[val]
	rst = 0
	for ch in str(val):
		rst += int(ch) ** 2
	return rst

for i in range(1, maxi):
	val = i
	while val not in [1, 89]:
		val = maquethmsq(val)
	if val == 89:
		total += 1
	S[i] = val
print(total)