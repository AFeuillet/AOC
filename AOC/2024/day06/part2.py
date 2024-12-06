import copy
from os import system
from time import sleep

nfile = open('data.txt', 'r')
base = nfile.read().split('\n')
plan = []
i = 0

for b in base:
  posb = b.find('^')
  if posb != -1:
    initpos = [i, posb, '^']
  plan.append(list(b))
  i += 1

leni = len(plan)
lenj = len(plan[0])
base_plan = copy.deepcopy(plan)
poslist = {}

def getnexpos(pos, pl):
   i, j, cur = pos
   lkey = '{}-{}'.format(i, j)
   if lkey not in poslist:
      poslist[lkey] = []
   if cur in poslist[lkey]:
      return [-2, -2, 'L']
   poslist[lkey].append(cur)
   
   pl[i][j] = 'X'
   if cur == '^':
      if i - 1 < 0:
         return [-1, -1, '']
      if pl[i - 1][j] == '#':
         return [i, j, '>']
      pl[i - 1][j] = '^'
      return [i - 1, j, '^']
   elif cur == '>':
      if j + 1 >= lenj:
         return [-1, -1, '']
      if pl[i][j + 1] == '#':
         return [i, j, 'v']
      pl[i][j + 1] = '>'
      return [i, j + 1, '>']
   elif cur == 'v':
      if i + 1 >= leni:
         return [-1, -1, '']
      if pl[i + 1][j] == '#':
         return [i, j, '<']
      pl[i + 1][j] = 'v'
      return [i + 1, j, 'v']
   elif cur == '<':
      if j - 1 < 0:
        return [-1, -1, '']
      if pl[i][j - 1] == '#':
        return [i, j, '^']
      pl[i][j - 1] = '<'
      return [i, j - 1, '<']  

def displayit(pl):
    for p in pl:
        print(''.join(p))
    print()

pos = initpos
while True:
   pos = getnexpos(pos, plan)
   if pos[0] < 0:
      break

total = 0
old = [-1, -1]
for i, p in enumerate(plan):
   for j, block in enumerate(p):
      if block == 'X':
         tmp_plan = copy.deepcopy(base_plan)
         tmp_plan[i][j] = '#'
         pos = initpos
         poslist = {}
         while True:
            pos = getnexpos(pos, tmp_plan)
            if pos[0] < 0:
               break
         if pos[0] == -2:
            old = [i, j]
            total += 1
print(total)

