nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
def isok(res, elts, pos, op, subt):
  if subt > res:
    return False
  if pos == len(elts):
    if subt == res: 
      return True
    return False
  if op == '*':
    subt *= elts[pos]
  else:
    subt += elts[pos]
  return isok(res, elts, pos + 1, '*', subt) or isok(res, elts, pos + 1, '+', subt)

for b in base:
  rb = b.split(': ')
  res = int(rb[0])
  elts = list(map(int, rb[1].split(' ')))

  if isok(res, elts, 0, '+', 0):
    total += res
print(total)