a = 1
b = 2
old = 0
i = 0
while True:
    old = b
    b = a + b
    a = old
    if len(str(b)) == 1000:
        print(i+4)
        exit()
    i += 1
