maxnb = 1000000
longestChain = 0

for num in range(maxnb):
    n = num
    total = 1
    while (n > 1):
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3*n + 1
        total += 1
    if total > longestChain:
        longestChain = total
        longestNum = num

print(longestNum)