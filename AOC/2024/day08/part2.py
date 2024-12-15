nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
plan_base = []
antenas = {}
antinodes = set()
LI, LJ = len(base), len(base[0])

def setantinode(c, p):
  for a in antenas[c]:
    di = abs(p[0] - a[0])
    dj = abs(p[1] - a[1])
    antinode = [[-1, -1], [-1, -1]]
    if a[0] > p[0]:
      antinode[0][0] = p[0] - di
      antinode[1][0] = a[0] + di
    else:
      antinode[0][0] = p[0] + di
      antinode[1][0] = a[0] - di
    if a[1] > p[1]:
      antinode[0][1] = p[1] - dj
      antinode[1][1] = a[1] + dj
    else:
      antinode[0][1] = p[1] + dj
      antinode[1][1] = a[1] - dj

    while antinode[0][0] >= 0 and antinode[0][1] >= 0 and antinode[0][0] < LI and antinode[0][1] < LJ:
      antinodes.add(tuple(antinode[0]))
      if a[0] > p[0]:
        antinode[0][0] = antinode[0][0] - di
      else:
        antinode[0][0] = antinode[0][0] + di
      if a[1] > p[1]:
        antinode[0][1] = antinode[0][1] - dj
      else:
        antinode[0][1] = antinode[0][1] + dj
    while antinode[1][0] >= 0 and antinode[1][1] >= 0 and antinode[1][0] < LI and antinode[1][1] < LJ:
      antinodes.add(tuple(antinode[1]))
      if a[0] > p[0]:
        antinode[1][0] = antinode[1][0] + di
      else:
        antinode[1][0] = antinode[1][0] - di
      if a[1] > p[1]:
        antinode[1][1] = antinode[1][1] + dj
      else:
        antinode[1][1] = antinode[1][1] - dj
  return

for i, b in enumerate(base):
  plan_base.append(list(b))
  for j, c in enumerate(list(b)):
    if c != '.':
      if c not in antenas:
        antenas[c] = []
      setantinode(c, [i, j])
      antenas[c].append([i, j])

for a in antinodes:
  plan_base[a[0]][a[1]] = '#'
for p in plan_base:
  total += LJ - p.count('.')
print(total)