nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

location0, location1 = [], []
total = 0

for data in datas:
    numbers = data.split('  ')
    location0.append(int(numbers[0]))
    location1.append(int(numbers[1]))

for loc in location0:
    total += loc * location1.count(loc)
print(total)