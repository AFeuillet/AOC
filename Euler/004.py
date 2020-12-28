def ispalindrome(n):
    digits = [int(d) for d in str(n)]
    dlen = len(digits)
    for i in range(0, int(dlen/2)):
        if digits[i] != digits[dlen -i -1]:
            return False
    return True

start = 100
maxi = 1000
pal = 0

for a in range (start, maxi):
    for b in range (start, maxi):
        mul = a * b
        if ispalindrome(mul) and mul > pal:
            pal = mul
            print("a: %s, b: %s, pal: %s" % (a, b, pal))
print(pal)
