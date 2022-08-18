"""
       /|
      / | c2
     /__|
 b  /| d| 
   / |  |
  /  |  | c1
 /   |  |
/)___|__| 
    a

"""
maxi = 99999
total = 0
target = 1000000

for a in range(1 , maxi + 1):
	for c1 in range(1, a + 1):
		for c2 in range(c1, a + 1):
			if sqrt((c1 + c2) ** 2 + a ** 2).is_integer():
				total += 1
				if total > target:
					print(a)
					exit()