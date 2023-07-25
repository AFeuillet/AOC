total = 0
for powed in range(100):
	i = 1
	while len(str(pow(i, powed))) <= powed:
		if len(str(pow(i, powed))) == powed:
			total += 1
		i += 1
print(total)