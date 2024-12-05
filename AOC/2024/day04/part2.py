nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
cc = []
for b in base:
  cc.append(list(b))

leni = len(cc)
lenj = len(cc[0])

def readXmas(i, j):
  xs = 2
  if j + xs < lenj and i + xs < leni:
      if cc[i + 1][j + 1] == 'A' and ((cc[i][j] == 'M' and cc[i + 2][j + 2] == 'S') or (cc[i][j] == 'S' and cc[i + 2][j + 2] == 'M')):
          if (cc[i + 2][j] == 'M' and cc[i][j + 2] == 'S') or (cc[i + 2][j] == 'S' and cc[i][j + 2] == 'M'):
            return 1
  return 0

for i in range(leni):
  for j in range(lenj):
    total += readXmas(i, j)
print(total)