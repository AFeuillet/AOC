maxnb = 1000001
strto = ''
for i in range(0, maxnb):
    strto += str(i)
print(int(strto[1]) * int(strto[10]) * int(strto[100]) * int(strto[1000]) * int(strto[10000]) * int(strto[100000]) * int(strto[1000000]))