import math

a = 1
b = 1
c = 1
maxi = 999
nbfind = 1000

for a in range(1, maxi):
    for b in range(a, maxi):
        c = math.sqrt(a**2 + b**2)
        if (c.is_integer() and c > a and c > b and  a + b + c == nbfind):
            print("a: %s, b: %s, c: %s, a*b*c: %s" % (a, b, c, a * b * c) )
            exit()
