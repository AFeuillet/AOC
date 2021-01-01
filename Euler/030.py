from utils import *


total = 0
#295245 = (9 ** 5) * 5
for i in range(10, 295245):
    digi = to_digit(i)
    fifths = 0
    for a in digi:
     	fifths += int(a) ** 5
    if (i == fifths):
        total += i
        print(i)
print("Sum", total)
