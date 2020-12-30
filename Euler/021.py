import math
from utils import *

maxnb = 10000
total = 0
total_arr = [None] * maxnb

for i in range(1, maxnb):
    if total_arr[i] == None:
        total_arr[i] = proper_sum(i)
    if total_arr[i] < maxnb and i != total_arr[i]:
        if total_arr[total_arr[i]] == None:
            total_arr[total_arr[i]] = proper_sum(total_arr[i])
        if total_arr[total_arr[i]] == i:
            total+=i
            print("a:%s b:%s"%(i, total_arr[i]))

print(total)