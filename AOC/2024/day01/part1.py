nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

location0, location1 = [], []
total = 0

for data in datas:
    numbers = data.split('  ')
    location0.append(int(numbers[0]))
    location1.append(int(numbers[1]))
location0.sort()
location1.sort()

for i in range(len(location0)):
    total += abs(location0[i] - location1[i])
print(total)