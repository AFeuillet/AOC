from utils import *

# First Method but pwd too long 
"""
pasw = []
for line in load_data('079'):
	if line not in pasw:
		pasw.append(line)

pasw.sort()
paswcode = pasw[0]
for hint in pasw:
	i = 0
	for c in paswcode:
		if i < len(hint) and hint[i] == c:
			i += 1
	for j in range(i, 3):
		paswcode += hint[j]

print(paswcode)
"""

# Second Method by hand
lst = {}
for i in range(10):
	lst[str(i)] = {'<': set(), '>': set()}

for line in load_data('079'):
	lst[line[0]]['<'].add(line[1])
	lst[line[0]]['<'].add(line[2])

	lst[line[1]]['<'].add(line[2])
	lst[line[1]]['>'].add(line[0])

	lst[line[2]]['>'].add(line[0])
	lst[line[2]]['>'].add(line[1])

print(lst)