from utils import *

"""
k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

"""

# Reccursing taking too long
"""
maxi = 1200
setf = set()
def msch(k, nbt, m, s):
	global minf
	if nbt - 1 != 0:
		if m > k ** 2 or m > minf or s > minf:
			return minf
		for i in range(1, k):
			msch(k, nbt - 1, m * i, s + i)
	elif m == s and m < minf:
		minf = m
		return minf

for k in range(2, maxi):
	minf = 2 * k
	msch(k + 1, k + 1, 1, 0)
	setf.add(minf)
	print(k + 1,minf)
print(sum(i for i in setf))
"""


""""
# check if a number is a product sum number ex 8 = 2x2x2x1x... = 2+2+2+1...
# Cannot work for primes
for i in range(3, maxi * 2):
	print(i)
	if not is_prime(i):
		#addtok(i, prime_factors(i))
		for j in range(2, int(i / 2) + 1):
			if i % j == 0:
				addtok(i, [i // j, j])
"""
maxi = 12000
setk = [maxi ** 2] * maxi

def addtok(m, s, c, i):
	k = m - s + c
	if k < maxi:
		setk[k] = min(m, setk[k])
		for j in range(i, maxi // m * 2 + 1):
			addtok(m * j, s + j, c + 1, j)
addtok(1, 1, 1, 2)
print(sum(set(setk[2:])))