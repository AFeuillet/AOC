import copy

nfile = open('data/day12.txt', 'r')
nbl = nfile.read().split('\n')

caves = {}
def addToCave(inp, outp):
	if inp not in caves:
		caves[inp] = {
			'caves': [], 
			'pas': 2 if inp.islower() else float('inf')
		}
	caves[inp]['caves'].append(outp)

for line in nbl:
	ic, oc = line.split('-')
	addToCave(ic, oc)
	addToCave(oc, ic)
	caves['MiniCave'] = True

def explore(currentCave, newcaves, total):
	if currentCave == 'end':
		return total + 1

	newcaves = copy.deepcopy(newcaves)
	caveTemp = newcaves[currentCave]

	if currentCave != 'start':
		newcaves[currentCave]['pas'] -= 1
		if newcaves[currentCave]['pas'] == 0:
			newcaves['MiniCave'] = False
			for smallcave in list(newcaves.keys()):
				if smallcave != 'MiniCave' and newcaves[smallcave]['pas'] == 1:
					newcaves.pop(smallcave)
		if not newcaves['MiniCave'] and newcaves[currentCave]['pas'] < 2:
			newcaves.pop(currentCave)
	else:
		newcaves.pop(currentCave)

	for cave in caveTemp['caves']:
		if cave in newcaves:
			total = explore(cave, newcaves, total)
	return total

print('Part Two: %s' % explore('start', caves, 0))