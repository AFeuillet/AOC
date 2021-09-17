import re

nfile = open('data/day06.txt', 'r')

nbsiz = 1000
lights = [[False for x in range(nbsiz)] for y in range(nbsiz)]
nbl = nfile.read().split('\n')
r = re.compile(r'(\bturn off\s\b|\bturn on\s\b|\btoggle\s\b)(\d+),(\d+)\sthrough\s(\d+),(\d+)')

for untre in nbl:
    grp = r.findall(untre)[0]
    action = grp[0]
    y0 = int(grp[1])
    y1 = int(grp[3])
    x0 = int(grp[2])
    x1 = int(grp[4])
    if action == 'turn off ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] = False
    elif action == 'turn on ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] = True
    elif action == 'toggle ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] = not lights[x][y]
total = 0
for i in range(nbsiz):
    for j in range(nbsiz):
        if lights[i][j]:
            total += 1
print("Part One: %s" % total)


lights = [[0 for x in range(nbsiz)] for y in range(nbsiz)]
for untre in nbl:
    grp = r.findall(untre)[0]
    action = grp[0]
    y0 = int(grp[1])
    y1 = int(grp[3])
    x0 = int(grp[2])
    x1 = int(grp[4])
    if action == 'turn off ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] -= 1
                if lights[x][y] < 0:
                    lights[x][y] = 0
    elif action == 'turn on ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] += 1
    elif action == 'toggle ':
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                lights[x][y] += 2
total = 0
for i in range(nbsiz):
    for j in range(nbsiz):
        total += lights[i][j]
print("Part Two: %s" % total)

