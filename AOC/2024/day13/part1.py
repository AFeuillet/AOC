import math
import re
nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

i = 0
total = 0
maxp = 100
for b in base:
  if i == 0:
    ax, ay = list(map(int, re.findall(r'\+(\d+)', b)))
  elif i == 1:
    bx, by = list(map(int, re.findall(r'\+(\d+)', b)))
  elif i == 2:
    X, Y = list(map(int, re.findall(r'\=(\d+)', b)))
  elif i == 3:
    token = math.inf
    for ai in range(1, maxp, 1):
      for bi in range(1, maxp, 1):  
        ar = ai * ax + bi * bx
        br = ai * ay + bi * by
        if ar == X and br == Y:
          token = min(token, (3 * ai + 1 * bi))
          break
        elif ar > X or br > Y:
          break        
    if token < math.inf:
      total += token
    i = -1
  i += 1
print(total)