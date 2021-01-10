from utils import *


"""
0: High Card: Highest value card.
1: One Pair: Two cards of the same value.
2: Two Pairs: Two different pairs.
3: Three of a Kind: Three cards of the same value.
4: Straight: All cards are consecutive values.
5: Flush: All cards of the same suit.
6: Full House: Three of a kind and a pair.
7: Four of a Kind: Four cards of the same value.
8: Straight Flush: All cards are consecutive values of same suit.
9: Royal Flush
"""
parties =[]
for line in load_data('054'):
	parties.append(line.split(' '))

def definehand(cards):
	hand = {}
	hand['init'] = cards
	hand['cards'] = []
	hand['suited'] = True
	color = cards[0][1:2]
	maxcount = 0
	cardtoadd = 0
	for card in cards:
		if color != cards[1:2]:
			hand['suited'] = False
		if card[0:1] == 'T':
			cardtoadd = 10
		elif card[0:1] == 'J':
			cardtoadd = 11
		elif card[0:1] == 'Q':
			cardtoadd = 12
		elif card[0:1] == 'K':
			cardtoadd = 13
		elif card[0:1] == 'A':
			cardtoadd = 14
		else:
			cardtoadd = int(card[0:1])
		hand['cards'].append(cardtoadd)
		maxcount = max(maxcount, hand['cards'].count(cardtoadd))
	hand['cards'].sort(reverse=True)
	hand['unikcard'] = list(set(hand['cards']))
	hand['unik'] = len(hand['unikcard'])
	hand['weight'] = {}
	for ucard in hand['unikcard']:
		if hand['cards'].count(ucard) not in hand['weight']:
			hand['weight'][hand['cards'].count(ucard)] = []
		hand['weight'][hand['cards'].count(ucard)].append(ucard)
	hand['cardz'] = []
	if hand['unik'] == 5:
		hand['cardz'] = hand['cards']
		if (hand['cards'][0] - hand['cards'][4] == 4 or hand['cards'] == [14, 5, 4, 3, 2]):
			if hand['suited']:
				hand['value'] = 8
			else:
				hand['value'] = 4
		elif hand['suited']:
			hand['value'] = 5
		else:
			hand['value'] = 0
	elif hand['unik'] == 4:
		hand['cardz'] = hand['weight'][2] + sorted(hand['weight'][1], reverse=True)
		hand['value'] = 1
	elif hand['unik'] == 3:
		if maxcount == 2:
			hand['cardz'] = sorted(hand['weight'][2], reverse=True) + sorted(hand['weight'][1], reverse=True)
			hand['value'] = 2
		elif maxcount == 3:
			hand['cardz'] = hand['weight'][3] + sorted(hand['weight'][1], reverse=True)
			hand['value'] = 3
	elif hand['unik'] == 2:
		if maxcount == 4:
			hand['cardz'] = hand['weight'][4] + hand['weight'][1]
			hand['value'] = 7
		elif maxcount == 3:
			hand['cardz'] = hand['weight'][3] + hand['weight'][2]
			hand['value'] = 6
	return hand

def onewin(pone, ptwo):
	if pone['value'] == ptwo['value']:
		for i in range(5):
			if pone['cardz'][i] != ptwo['cardz'][i]:
				return pone['cardz'][i] > ptwo['cardz'][i]
	else:
		return pone['value'] > ptwo['value']

total = 0
for party in parties:
	playerone = definehand(party[:5])
	playertwo = definehand(party[5:])
	if onewin(playerone, playertwo):
		total += 1

print(total)