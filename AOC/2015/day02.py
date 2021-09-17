nfile = open('data/day02.txt', 'r')
nbl = nfile.read().split('\n')

total = 0
total2 = 0
for line in nbl:
	l, w, h = [int(x) for x in line.split('x')]
	total += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
	total2 += ((l + w + h) - max(l, w, h)) * 2 + l * w * h

print("Part One: %s" % (total))
print("Part Two: %s" % (total2))
