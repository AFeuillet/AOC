def digit_sum(n):
    sum = 0
    for d in str(n):
         sum+=int(d)
    return sum

maxnb = 100
total = 0
for a in range(1, maxnb):
    for b in range(1, maxnb):
        total = max(digit_sum(a ** b), total)
print(total)