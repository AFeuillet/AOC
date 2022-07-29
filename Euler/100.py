def getOdd(nb_blue, nb_total):
	return round( ( (nb_blue / nb_total) * (( nb_blue - 1 ) / (nb_total - 1) ) ), 15)

# Tests
print(getOdd(15, 21))
print(getOdd(85, 120))

# BrutForce Solution
"""
for nb_total in range(10**12, 10**13): # Too Long
	for i in range(1, nb_total):
		if getOdd(i, nb_total) == 0.5:
			print('Number of blues: %s total: %s ' % (i, nb_total) )
			exit()
"""

# Equation Solution 
# x-> blue y-> total
# x*(x-1) / (y*(y-1)) = 1/2 
# --> 2x**2 - 2x - y**2 + y = 0 
# --> Diophantienne Equation
# --> xn+1 = 3 ⁢xn + 2 ⁢yn - 2 ⁢ yn+1 = 4 ⁢xn + 3 ⁢yn - 3 ⁢
x = 15
y = 21

while(y <  10 ** 12):
	blue = 3 * x + 2 * y - 2
	total = 4 * x + 3 * y - 3 
	print('Number of blues: %s total: %s ' % (blue, total) )
	x = blue
	y = total