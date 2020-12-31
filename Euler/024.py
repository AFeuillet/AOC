import itertools


allperm = list(itertools.permutations("0123456789"))
million = ''.join(allperm[999999])
print(million)