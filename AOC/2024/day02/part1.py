nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0

def is_valid(line):
  asc = 1
  if line[0] < line[1]:
    asc = 0
  for i in range(len(line) - 1):
    if abs(line[i] - line[i + 1]) > 3:
      return False
    if line[i] >= line[i + 1] and asc == 0:
      return False
    if line[i] <= line[i + 1] and asc == 1:
      return False
  return True

for data in datas:
  if is_valid(list(map(int, data.split(' ')))):
    total += 1
print(total)