from decimal import Decimal as D
import math

"""
https://en.wikipedia.org/wiki/Heronian_triangle#Almost-equilateral_Heronian_triangles

   /\
a /  \
 /____\
   c

cos(?) = (c/2)/a
h = sin(?) * a

First:
a c p +- area
5 6 16 +1 12
17 16 50 -1 120
65 66 196 +1 1848 
241 240 722 -1 25080
901 902 2704 +1 351780
3361 3360 10082 -1 4890480
12545 12546 37636 +1 68149872
46817 46816 140450 -1 949077360
174725 174726 524176 +1 13219419708
"""

# Heron's Formula
# Not working after 1000000 due to precision
def area1(a, c, p):
	hp = p * 0.5
	ssq = hp * (hp - c) * (hp - a) * (hp - a)
	if(a == 490240 and c == 490239):
		print(hp, format(ssq,'f'), math.sqrt(ssq))
	return is_square(ssq)
	return math.sqrt(ssq) % 1 == 0

# Not working after 1000000 due to precision
def area2(a, c, p):
	ssq = (c + a * 2 ) * D(a * 2 - c) * c ** 2
	sq = 0.25 * math.sqrt(ssq)
	if(a == 490240 and c == 490239):
		print(ssq, format(sq,'f'), math.sqrt(ssq))
	return sq % 1 == 0

# Not working after 1000000 due to precision
def area3(a, c, p):
	h = math.sin(math.acos((c / 2) / a)) * a
	are = D(D(h) * D(c) / 2)
	if(a == 468106 and c == 468105):
		print(are, h, D(h) * D(c), math.acos((c / 2) / a), (c / 2) / a)
	return are % 1 == 0

maxi = 1000000000
total = 0

"""
First method brut force
for i in range(2, int(maxi / 3)):
	if i % 100000000 == 0:
		print(i, total)
	per = i * 3
	area = area1(i, i + 1, per + 1)
	if area:
		total += per + 1
		print(i,i + 1, per + 1, '+1', (area))
	area = area1(i, i - 1, per - 1)
	if area:
		total += per - 1
		print(i,i - 1, per - 1, '-1', (area))
"""

a = 1
c = 1
p = -4
pm = 1

# Second method easy formula
while p <= maxi:
	tmpa = a
	a = c 
	c = 4 * c - tmpa + 2 * pm
	pm = - pm
	total += p
	p = 3 * a - pm

print(total)

