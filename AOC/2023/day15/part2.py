nfile = open('data.txt', 'r')
nbl = nfile.read().replace('\n', '').split(',')

boxes = [{'id': i, 'labels':[], 'values':[]} for i in range(256)]

def hashAlgo(txt):
	curval = 0
	for c in txt:
		curval += ord(c)
		curval *= 17
		curval %= 256
	return curval

def removeV(val):
	for l in boxes:
		if val in l['labels']:
			idx = l['labels'].index(val)
			l['labels'].remove(val)
			del l['values'][idx]

def addV(cur, lab, val):
	if lab in boxes[cur]['labels']:
		idx = boxes[cur]['labels'].index(lab)
		boxes[cur]['values'][idx] = int(val)
	else:
		boxes[cur]['labels'].append(lab)
		boxes[cur]['values'].append(int(val))

for nb in nbl:	
	cur = 0
	if '-' in nb:
		removeV(nb[:-1])
	else:
		adds = nb.split('=')
		box = hashAlgo(adds[0])
		addV(box, adds[0], adds[1])

total = 0
for box in boxes:
	if len(box['values']) > 0:
		for i in range(len(box['values'])):
			total += (box['id'] + 1) * (i + 1) * box['values'][i]
print(total)