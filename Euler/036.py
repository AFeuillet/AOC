from utils import *

maxnb = 1000000
total = 0

for i in range(maxnb):
    if is_palindrome(i) and is_palindrome(int(str(bin(i))[2:])):
        total += i
        print("Palindromic both base 10, 2: %s" % (i))
print("Total: %s" % (total))