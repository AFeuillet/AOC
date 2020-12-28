i = 2520

def canbdivide(number):
    for j in range(2, 20):
        if (number % j) != 0:
            return False
    return True

while True:
    if canbdivide(i):
        print(i)
        exit()
    i += 1    