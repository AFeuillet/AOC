import re
nfile = open('data.txt', 'r')
texte = nfile.read()
pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'

total = 0
rs = re.findall(pattern, texte)
enabled = True
for r in rs:
  if r == "don't()":
    enabled = False
  elif r == "do()":
    enabled = True
  elif enabled == True:
    mul = list(map(int, re.findall(r'\d+', r)))
    total += mul[0] * mul[1]

print(total)