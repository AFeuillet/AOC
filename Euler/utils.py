def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def ispalindrome(n):
    digits = [int(d) for d in str(n)]
    dlen = len(digits)
    for i in range(0, int(dlen/2)):
        if digits[i] != digits[dlen -i -1]:
            return False
    return True

def is_pandigital(n):
    a = [int(d) for d in str(n)]
    if len(a) > 9:
        return False
    a.sort()
    if a[0] == 0:
        return False
    for i in range(0, len(a)-1):
        if a[i] == a[i+1]:
            return False
    return True    

def to_digit(n):
    return [int(d) for d in str(n)]

def proper_divisor(n):
    a=[]
    for i in range(1, int(n/2)+1):
        if (n%i == 0):
            a.append(i)
    return a

def proper_sum(n):
    ar = proper_divisor(n)
    intotal = 0
    for a in ar:
        intotal += a
    return intotal

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors