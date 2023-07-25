
cub = {}
cubsmall = {}
cubmax = 100000
nbperm = 5
for i in range(100, cubmax):
	sortval = str(sorted(str(pow(i, 3))))
	cub[i] = sortval
	if sortval not in cubsmall:
		cubsmall[sortval] = pow(i, 3)
	if(list(cub.values()).count(sortval) == nbperm):
		print('Found i: %s val: %s' % (cubsmall[sortval], sortval))
		exit()