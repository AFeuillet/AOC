from functools import reduce
from math import sqrt


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    digits = [int(d) for d in str(n)]
    dlen = len(digits)
    for i in range(0, int(dlen / 2)):
        if digits[i] != digits[dlen - i - 1]:
            return False
    return True

def is_pandigital(n):
    a = [int(d) for d in str(n)]
    if len(a) > 9:
        return False
    a.sort()
    if a[0] == 0:
        return False
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            return False
    return True    

def is_pandigital2(n):
    a = [int(d) for d in str(n)]
    a.sort()
    if a[0] != 0 and a == range(1, len(a) + 1):
        return True
    return False    

def to_digit(n):
    return [int(d) for d in str(n)]

def proper_divisor(n):
    a=[]
    for i in range(1, int(n / 2) + 1):
        if (n % i == 0):
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

def factors_simple(number):
    nbd = 0
    for j in range(1, int(number / 2) + 1):
        if (number % j) == 0:
            nbd += 1
    return nbd + 1

def factors_optimized(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

def load_data(name):
    nfile = open('data/' + name + '.txt', 'r')
    return nfile.read().split('\n')