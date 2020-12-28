from utils import *


total = 0
for i in range(2000000):
    if is_prime(i):
        total += i
print(total)