nfile = open('data.txt', 'r')
nbl = nfile.read().split('\n')

hands = {}
def isStrongerThan(cards1, cards2):
	if cards1['type'] > cards2['type']:
		return True
	elif cards1['type'] == cards2['type']:
		for i in range(5):
			if cards1['cardv'][i] > cards2['cardv'][i]:
				return True
			elif  cards1['cardv'][i] < cards2['cardv'][i]:
				return False
	return False

def replaceCard(hand):
	hv = []
	repl = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}
	for h in hand:
		if h in repl.keys():
			hv.append(repl[h])
		else:
			hv.append(int(h))
	return hv

def getType(hand):
	cardav = list(set(hand))
	if 'J' in cardav:
		big = 'J'
		mx = 0
		for c in cardav:
			if c == 'J':
				continue
			count = hand.count(c)
			if count > mx:
				big = c 
				mx = count
		hand = hand.replace('J', big)
		cardav = list(set(hand))

	if len(cardav) == 1: # Five of a kind
		return 7
	if len(cardav) == 2: 
		fn = hand.count(cardav[0])
		if fn == 1 or fn == 4:
			return 6 # Four of a kind
		else: # 2 and 3
			return 5 # Full house
	elif len(cardav) == 3: 
		for c in cardav:
			if hand.count(c) == 3:
				return 4 # Three of a kind
		return 3 # Two pair
	elif len(cardav) == 4:
		return 2 # One pair
	elif len(cardav) == 5:
		return 1 # High card

sortd = []
for nb in nbl:
	hand = nb.split(' ')
	hands[hand[0]] = {
		'card': hand[0],
		'cardv': replaceCard(hand[0]),
		'bid': int(hand[1]),
		'type': getType(hand[0])
	}
	sortd.append(hand[0])

total = 0
for i in range(len(sortd) - 1):
	for j in range(len(sortd) - 1):
		if isStrongerThan(hands[sortd[j]], hands[sortd[j + 1]]):
			tmp = sortd[j + 1]
			sortd[j + 1] = sortd[j]
			sortd[j] = tmp
total = 0
for i in range(len(sortd)):
	total += hands[sortd[i]]['bid'] * (i + 1)

print(total)