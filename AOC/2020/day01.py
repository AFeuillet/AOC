nfile = open('data/day01.txt', 'r')
nbs = nfile.read().split('\n')

def dayOnea():
	for nb1 in nbs:
		for nb2 in nbs:
			if int(nb1) + int(nb2) == 2020:
				return  (nb1, nb2)
	return False

def dayOneb():
	for nb1 in nbs:
		for nb2 in nbs:
			for nb3 in nbs:
				if int(nb1) + int(nb2) + int(nb3) == 2020:
					return (nb1, nb2, nb3)
	return False

print(dayOnea())
print(dayOneb())
	