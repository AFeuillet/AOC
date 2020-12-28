maxnb = 4000000
a = 1
b = 2
old = 0
count = 0
for i in range(maxnb):
    if (b % 2) == 0:
        count += b
    old = b
    b = a + b
    a = old
    if a >= maxnb:
        print("Total", count)
        break;