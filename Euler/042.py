maxnb = 26
triangles = [0]
for i in range(1, maxnb + 1):
    triangles.append(int((i * (i + 1)) / 2))

def namesum(stro):
    subtotal = 0
    for i in range(len(stro)):
        subtotal += ord(stro[i].lower())-96
    return subtotal

nfile = open('data/042.txt', 'r')
names = nfile.read().replace('"','').split(',')

total = 0
for name in names:
    if namesum(name) in triangles:
        total+=1
print(total)
