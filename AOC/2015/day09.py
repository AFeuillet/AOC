import copy
import re

nfile = open('data/daytmp.txt', 'r')
nbl = nfile.read().split('\n')

def betterway(destinations, routes, total):
	for depart in destinations:
		dest2 = copy.deepcopy(destinations)
		dest2.remove(depart)
		if len(dest2) == 0:
			return total
		else:
			mintotal = 999999
			for arr in dest2:
				mintotal = min(betterway(dest2, routes, total + routes[depart][arr]), mintotal)
			return mintotal

destinations = set()
routes = {}
for route in nbl:
	r = re.compile(r"(.*) to (.*)\s=\s(\d+)")
	grp = r.findall(route)[0]
	destinations.add(grp[0])
	destinations.add(grp[1])
	if grp[0] not in routes:
		routes[grp[0]] = {}
	if grp[1] not in routes:
		routes[grp[1]] = {}
	routes[grp[0]][grp[1]] = int(grp[2])
	routes[grp[1]][grp[0]] = int(grp[2])

print("Part One: %s" % betterway(destinations, routes, 0))
print(destinations)
print(routes)
#371 too high