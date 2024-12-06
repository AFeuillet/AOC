from os import system
from time import sleep

nfile = open('data.txt', 'r')
base = nfile.read().split('\n')
plan = []
i = 0

for b in base:
  posb = b.find('^')
  if posb != -1:
    pos = [i, posb, '^']
  plan.append(list(b))
  i += 1

leni = len(plan)
lenj = len(plan[0])

def getnexpos(pos):
   i, j, cur = pos
   plan[i][j] = 'X'
   if cur == '^':
      if i - 1 < 0:
         return [-1, -1, '']
      if plan[i - 1][j] == '#':
         return [i, j, '>']
      plan[i - 1][j] = '^'
      return [i - 1, j, '^']
   elif cur == '>':
      if j + 1 >= lenj:
         return [-1, -1, '']
      if plan[i][j + 1] == '#':
         return [i, j, 'v']
      plan[i][j + 1] = '>'
      return [i, j + 1, '>']
   elif cur == 'v':
      if i + 1 >= leni:
         return [-1, -1, '']
      if plan[i + 1][j] == '#':
         return [i, j, '<']
      plan[i + 1][j] = 'v'
      return [i + 1, j, 'v']
   elif cur == '<':
      if j - 1 < 0:
        return [-1, -1, '']
      if plan[i][j - 1] == '#':
        return [i, j, '^']
      plan[i][j - 1] = '<'
      return [i, j - 1, '<']  

def displayit():
    system('clear')
    for p in plan:
        print(''.join(p))

while True:
   pos = getnexpos(pos)
   #displayit()
   if pos[0] < 0:
      break

total = 0
for p in plan:
   total += p.count('X')
print(total)

