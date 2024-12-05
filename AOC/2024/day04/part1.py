nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
cc = []
for b in base:
  cc.append(list(b))

leni = len(cc)
lenj = len(cc[0])

def readXmas(i, j):
  if cc[i][j] != 'X':
    return 0
  xs = 3
  st = 0
  if j + xs < lenj:
    if cc[i][j + 1] == 'M' and cc[i][j + 2] == 'A' and cc[i][j + 3] == 'S':
      st += 1
    if i + xs < leni:
      if cc[i + 1][j + 1] == 'M' and cc[i + 2][j + 2] == 'A' and cc[i + 3][j + 3] == 'S':
        st += 1
    if i - xs >= 0:
      if cc[i - 1][j + 1] == 'M' and cc[i - 2][j + 2] == 'A' and cc[i - 3][j + 3] == 'S':
        st += 1
  if j - xs >= 0:
    if cc[i][j - 1] == 'M' and cc[i][j - 2] == 'A' and cc[i][j - 3] == 'S':
      st += 1
    if i + xs < leni:
      if cc[i + 1][j - 1] == 'M' and cc[i + 2][j - 2] == 'A' and cc[i + 3][j - 3] == 'S':
        st += 1
    if i - xs >= 0:
      if cc[i - 1][j - 1] == 'M' and cc[i - 2][j - 2] == 'A' and cc[i - 3][j - 3] == 'S':
        st += 1
  if i - xs >= 0:
    if cc[i - 1][j] == 'M' and cc[i - 2][j] == 'A' and cc[i - 3][j] == 'S':
      st += 1
  if i + xs < leni:
    if cc[i + 1][j] == 'M' and cc[i + 2][j] == 'A' and cc[i + 3][j] == 'S':
      st += 1
  return st

for i in range(leni):
  for j in range(lenj):
    total += readXmas(i, j)
print(total)