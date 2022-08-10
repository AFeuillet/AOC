import copy
maxi = 1000
tr = []
sq = []
pe = []
hx = []
hp = []
oc = []
for n in range(maxi):
	trr = int((n * (n + 1)) / 2 )
	if trr < 10000 and trr > 999:
		tr.append(trr)
	sqq = n ** 2
	if sqq < 10000 and sqq > 999:
		sq.append(sqq)
	pee = int((n * (3 * n - 1)) / 2)
	if pee < 10000 and pee > 999:
		pe.append(pee)
	hxx = n * (2 * n - 1)
	if hxx < 10000 and hxx > 999:
		hx.append(hxx)
	hpp = int((n * (5 * n - 3)) / 2)
	if hpp < 10000 and hpp > 999:
		hp.append(hpp)
	occ = n * (3 * n - 2)
	if occ < 10000 and occ > 999:
		oc.append(occ)

def converta(lista):
	nset = {}
	for a in lista:
		a = str(a)
		f = a[:2]
		s = a[-2:]
		if f in nset:
			nset[f].append(s)
		else:
			nset[f] = [s]
	return nset

def findit(value, end, listc, parcours):
	if not listc:
		if value == end:
			print(parcours)
		return
	for li in listc:
		if value in S[li]:
			for v in S[li][value]:
				listd = copy.deepcopy(listc)
				listd.remove(li)
				findit(v, end, listd, parcours + int('%s%s' % (value, v)))

S ={'oc':converta(oc), 'tr': converta(tr), 'sq': converta(sq), 'pe': converta(pe), 'hx': converta(hx), 'hp': converta(hp)}

for item in S['oc'].items():
	found = False
	for ite in item[1]:
		findit(ite, item[0], ['tr', 'sq', 'pe', 'hx', 'hp'], int('%s%s' % (item[0], ite)))
