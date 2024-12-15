import math
import re
nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

i = 0
total = 0
for b in base:
  if i == 0:
    ax, ay = list(map(int, re.findall(r'\+(\d+)', b)))
  elif i == 1:
    bx, by = list(map(int, re.findall(r'\+(\d+)', b)))
  elif i == 2:
    X, Y = list(map(int, re.findall(r'\=(\d+)', b)))
    X += 10000000000000
    Y += 10000000000000
  elif i == 3:
    token = math.inf
    if ax == 0 or (ax * by) - (bx * ay) == 0:
      break
    else:
      bi = ((ax * Y) - (X * ay)) / ((ax  * by) - (ay * bx))
      ai = (X * ((ax  * by) - (ay * bx)) - ((ax * Y) - (X * ay)) * bx) / (((ax  * by) - (ay * bx)) * ax)
      if int(bi) == bi and int(ai) == ai:
        token = min(token, (3 * ai + 1 * bi))
    if token < math.inf:
      total += token
    i = -1
  i += 1
print(int(total))