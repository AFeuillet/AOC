num = 3
den = 2
total = 0
for i in range(1000):
	if len(str(num)) > len(str(den)):
		total += 1
	olden = den
	den = num + den
	num = den + olden
print(total)