import math
from utils import *

total = 0
num=1000
digs = to_digit(pow(2,num))
for i in digs:
    total += i
print(total)

