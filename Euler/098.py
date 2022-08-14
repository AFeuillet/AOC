from utils import *


def is_pairsq(word1, word2, sqar):
	lets = {}
	tabi = []
	curlen = len(word1)
	for i in range(curlen):
		if word1[i] in lets and lets[word1[i]] != sqar[i]:
			return False
		if sqar[i] in tabi and word1[i] not in lets:
			return False
		lets[word1[i]] = sqar[i]
		tabi.append(sqar[i])
	ns = ''
	for ch in word2:
		ns += lets[ch]
	if ns in S[curlen]['sqare']:
		return max(int(ns), int(sqar))
	return False

def is_pairword(word1, word2):
	for sqar in S[len(word1)]['sqare']:
		isp = is_pairsq(word1, word2, sqar)
		if isp is not False:
			return isp
	return False

line = load_data('098')
words = line[0].replace('"', '').split(',')
S = {}
lenw = 1
# Add word by length
for word in words:
	if len(word) not in S:
		S[len(word)] = {'words': [], 'anagram':[], 'anasqare':[], 'sqare':[]}
	S[len(word)]['words'].append(word)

anagram = []
maxlena = 0
# find all the anagrams and the maxlen possible
for words in S.items():
	for word1 in words[1]['words']:
		sword1 = sorted(word1)
		for word2 in words[1]['words']:
			if word1 != word2 and sword1 == sorted(word2) and (word2, word1) not in anagram:
				anagram.append((word1, word2))
				maxlena = max(maxlena, words[0])

lens = 1
i = 1
# compute all the sqare until max lengh
while lens <= maxlena:
	stri = str(i ** 2)
	lens = len(stri)
	S[lens]['sqare'].append(stri)
	i += 1

maxi = 0
# go through all anagram and tests every sqare number
for anag in anagram:
	ispx = is_pairword(anag[0], anag[1])
	if ispx is not False:
		maxi = max(maxi, ispx)

print(maxi)

