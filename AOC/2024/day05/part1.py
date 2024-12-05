nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
printlist = {}

def isok(cl):
   lcl = len(cl)
   for i in range(lcl):
      greater = set(printlist[cl[i]]['greaterthan'])
      lower = set(printlist[cl[i]]['lowerthan'])
      if not set(cl[:i]).issubset(lower) or not set(cl[i + 1:]).issubset(greater):
         return 0
   return int(cl[int(lcl/2)])

for b in base:    
    bl = b.split('|')
    if len(bl) == 2:
      if bl[0] not in printlist:
          printlist[bl[0]] = {'greaterthan': [], 'lowerthan': []}
      printlist[bl[0]]['greaterthan'].append(bl[1])
      if bl[1] not in printlist:
          printlist[bl[1]] = {'greaterthan': [], 'lowerthan': []}
      printlist[bl[1]]['lowerthan'].append(bl[0])
    elif b != '':
        cl = b.split(',')
        total += isok(cl)

print(total)