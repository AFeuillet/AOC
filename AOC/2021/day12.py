import copy

nfile = open('data/day12.txt', 'r')
nbl = nfile.read().split('\n')

caves = {}
def addToCave(inp, outp):
	if inp not in caves:
		caves[inp] = []
	caves[inp].append(outp)

for line in nbl:
	ic, oc = line.split('-')
	addToCave(ic, oc)
	addToCave(oc, ic)

def explore(currentCave, newcaves, total):
	if currentCave == 'end':
		return total + 1
	newcaves = copy.deepcopy(newcaves)
	caveTemp = newcaves[currentCave]
	if currentCave.islower():
		newcaves.pop(currentCave)	
	for cave in caveTemp:
		if cave in newcaves:
			total = explore(cave, newcaves, total)
	return total

print('Part One: %s' % explore('start', caves, 0))