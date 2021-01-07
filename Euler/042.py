maxnb = 26
total = 0

t = [0]
for i in range(1, maxnb + 1):
    t.append(int((i * (i + 1)) / 2))

def namesum(stro):
    subtotal = 0
    for i in range(len(stro)):
        subtotal += ord(stro[i].lower())-96
    return subtotal

nfile = open('data/042.txt', 'r')
names = nfile.read().replace('"','').split(',')

for name in names:
    if namesum(name) in t:
        total+=1
print(total)
