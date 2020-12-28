from utils import *

nbtofind=10001
nbprime=0
i = 1
while True:
    if is_prime(i):
        nbprime += 1
    if nbprime == nbtofind:
        print(i)
        exit()
    i += 1
