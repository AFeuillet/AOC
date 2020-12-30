numbers = {
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five',
	6 : 'six',
	7 : 'seven',
	8 : 'eight',
	9 : 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100:'hundred',
	1000:'thousand',
}

def lesshundnb(i):
	if i in numbers:
		return numbers[i]
	elif i < 100:
		return numbers[(i / 10) * 10] + numbers[i % 10]
	return False

total = 0
for i in range(1, 1000):
	if i < 100:
		nbstr = lesshundnb(i)
	elif i % 100 == 0:
		nbstr = numbers[(i / 100)] + numbers[100]
	else:
		nbstr = numbers[(i / 100)] + numbers[100] + 'and' + lesshundnb(i % 100)
	total += len(nbstr)
	print("i: %s, %s" % (i, nbstr))
total += len('onethousand')
print("Total: %s" % (total))