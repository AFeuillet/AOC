nbl = open('data.txt').read().split('\n')
total1, total2 = 0, 0
rules1 = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
rules2 = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
for nb in nbl:
	total1 += rules1[nb]
	total2 += rules2[nb]
print('Part 1: {}, Part 2: {}'.format(total1, total2))