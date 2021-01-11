from utils import *


parties =[]
data = load_data('059')
chars = list(map(int, data[0].split(',')))

"""
a=97
z=122
Char 32->125
"""
x = list(range(97, 123))
y = list(range(97, 123))

#Last char should be a dot
for i in x:
	if chr(i ^ chars[len(chars) - 1]) == '.':
		print("Third char is: %s" % (i))

#First char should be an uppercase
for i in y:
	if i ^ chars[0] < 65 or i ^ chars[0] > 90:
		x.remove(i)

#Remove unvalid char
for i in range(97, 123):
	for j in range(0, len(chars), 3):
		if i ^ chars[j] > 125 or i ^ chars[j] < 32:
			if i in x:
				x.remove(i)
		if i ^ chars[j + 1] > 125 or i ^ chars[j + 1] < 32:
			if i in y:
				y.remove(i)

#Show possibilities
for a in x:
	for b in y:
		print("-------%s-%s--------" % (a, b))
		for i in range(0, len(chars), 3):
			print(chr(a ^ chars[i]), end = '')
			print(chr(b ^ chars[i + 1]), end = '')
			print(chr(112 ^ chars[i + 2]), end = '')
		print("-------------------")

print(x)
print(y)

total = 0
for i in range(0, len(chars), 3):
	total += 101 ^ chars[i]
	total += 120 ^ chars[i + 1]
	total += 112 ^ chars[i + 2]
print(total)