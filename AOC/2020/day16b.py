from os import system
from time import sleep
import re
import pdb

nfile = open('data/day16.txt', 'r')
nbl = nfile.read().split('\n\n')
rulines = nbl[0].split('\n')

#Adding rules without name
rules = []
for line in rulines:
	a = line.split(': ')
	b = a[1].split(' or ')
	rules.append(b[0])
	rules.append(b[1])

nearbytickets = nbl[2].split('\n')

#Check if rules works
def inthat(rules, chk):
	for rule in rules:
		(amin, amax) = rule.split('-')
		if chk >= int(amin) and chk <= int(amax):
			return True
	return False

total = 0
goodtickets = []
nearbytickets.pop(0)

#Retrieving Good Tickets
for line in nearbytickets:
	chks = list(map(int, line.split(',')))
	adding = True
	for chk in chks:
		if not inthat(rules, chk):
			total += chk
			adding = False
	if adding:
		goodtickets.append(chks)

#Adding full rules
newrules = dict()
for line in rulines:
	a = line.split(': ')
	b = a[1].split(' or ')
	newrules[a[0]] = dict()
	newrules[a[0]]['rules'] = []
	newrules[a[0]]['rules'].append(b[0])
	newrules[a[0]]['rules'].append(b[1])
	newrules[a[0]]['pos'] = []

myticketline = nbl[1].split('\n')
myticket = list(map(int, myticketline[1].split(',')))

#Init with own ticket
for i in range(len(myticket)):
	for roule in newrules.iteritems():
		val = myticket[i]
		if inthat(roule[1]['rules'], val):
			roule[1]['pos'].append(i)

#Intersec withall good ticket
for ticket in goodtickets:
	for i in range(len(ticket)):
		for roule in newrules.iteritems():
			val = ticket[i]
			if not inthat(roule[1]['rules'], val):
				roule[1]['pos'].remove(i)

#Find one pos by rule
notdone = True
while notdone:
	notdone = False
	for roula in newrules.iteritems():
		if len(roula[1]['pos']) == 1:
			ktor = roula[1]['pos'][0]
			for roulb in newrules.iteritems():
				if len(roulb[1]['pos']) != 1 and ktor in roulb[1]['pos']:
					roulb[1]['pos'].remove(ktor)
		else:
			notdone = True

total = 1
print(myticket)
for n in newrules.iteritems():
	print(n)
	if 'departure' in n[0]:
		total *= myticket[n[1]['pos'][0]]
print(total)

