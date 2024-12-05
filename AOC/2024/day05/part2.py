nfile = open('data.txt', 'r')
base = nfile.read().split('\n')

total = 0
printlist = {}

def isok(cl):
   lcl = len(cl)
   for i in range(lcl):
      greater = printlist[cl[i]]['greaterthan']
      lower = printlist[cl[i]]['lowerthan']
      if not set(cl[:i]).issubset(lower) or not set(cl[i + 1:]).issubset(greater):
         return 0
   return int(cl[int(lcl/2)])

def inters(list1, list2):
   return [x for x in list1 if x in list2]

def reorder(cl):
   if len(cl) == 0:
      return cl
   gr = inters(cl[0:], printlist[cl[0]]['greaterthan'])
   lr = inters(cl[0:], printlist[cl[0]]['lowerthan'])
   return reorder(lr) + [cl[0]] + reorder(gr)

for b in base:    
    bl = b.split('|')
    if len(bl) == 2:
      if bl[0] not in printlist:
          printlist[bl[0]] = {'greaterthan': set(), 'lowerthan': set()}
      printlist[bl[0]]['greaterthan'].add(bl[1])
      if bl[1] not in printlist:
          printlist[bl[1]] = {'greaterthan': set(), 'lowerthan': set()}
      printlist[bl[1]]['lowerthan'].add(bl[0])
    elif b != '':
        cl = b.split(',')
        if isok(cl) == 0:
           total += isok(reorder(cl))

print(total)