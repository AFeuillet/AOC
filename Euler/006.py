maxi = 100
som1 = 0
som2 = 0

for i in range(1, maxi + 1):
    som1 += i**2
    som2 += i

print(som2**2 - som1)
