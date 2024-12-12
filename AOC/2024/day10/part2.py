nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
mapc = []
for b in base:
  mapc.append(list(map(int, list(b))))

LI = len(mapc)
LJ = len(mapc[0])

trailreach = set()
totaltrail = 0
def nbtrail(hdi, hdj, hdv):
  if hdv == 9:
    global totaltrail
    totaltrail += 1
    trailreach.add((hdi, hdj))
    return 1
  nxt = hdv + 1
  if hdi - 1 >= 0 and mapc[hdi - 1][hdj] == nxt:
    nbtrail(hdi - 1, hdj, nxt)
  if hdi + 1 < LI and mapc[hdi + 1][hdj] == nxt:
    nbtrail(hdi + 1, hdj, nxt)
  if hdj - 1 >= 0 and mapc[hdi][hdj - 1] == nxt:
    nbtrail(hdi, hdj - 1, nxt)
  if hdj + 1 < LJ and mapc[hdi][hdj + 1] == nxt:
    nbtrail(hdi, hdj + 1, nxt)
  return 0

for i, line in enumerate(mapc):
  for j, l in enumerate(line):
    if l == 0:
      nbtrail(i, j, l)
      total += len(trailreach)
      trailreach = set()

print(total)
print(totaltrail)