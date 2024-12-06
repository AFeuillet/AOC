import re
nfile = open('data.txt', 'r')
texte = nfile.read()
pattern = r'mul\(\d{1,3},\d{1,3}\)'

total = 0
rs = re.findall(pattern, texte)
for r in rs:
  mul = list(map(int, re.findall(r'\d+', r)))
  total += mul[0] * mul[1]

print(total)