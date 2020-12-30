import math
from utils import *


total = 0
for digit in to_digit(math.factorial(100)):
    total += digit
print(total)
