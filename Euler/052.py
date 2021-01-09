i = 1
while True:
	if (sorted(str(i)) == sorted(str(i * 2)) and 
		sorted(str(i)) == sorted(str(i * 3)) and 
		sorted(str(i)) == sorted(str(i * 4)) and 
		sorted(str(i)) == sorted(str(i * 5)) and 
		sorted(str(i)) == sorted(str(i * 6))):
		print("Permuted multiple number: %s" % (i))
		exit()
	i += 1