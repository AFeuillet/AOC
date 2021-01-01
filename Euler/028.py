diag = 1
total = 1
for n in range(2, 1002, 2):
	for i in range(4):
		diag += n
		total += diag
print(total)