nfile = open('data/022.txt', 'r')
names = nfile.read().replace('"', '').split(',')

names.sort()
total = 0
for i in range(len(names)):
	count = 0
	for letter in names[i]:
		count += ord(letter) - 64
	total += count * (i + 1)

print("Total: %s" % (total))