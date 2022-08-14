import math

maxi = 1000001
closest = 2 / 5
closnumerator = 2

# n / d
for n in range(1, maxi):
	for d in range(int(n * (7/3)), maxi):	
		if  n / d < closest:
			break
		if n / d < 3 / 7 and n / d > closest:
			if math.gcd(n, d) == 1:
				closest = n / d
				closnumerator = n
	
print(closnumerator)
