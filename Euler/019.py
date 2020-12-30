import datetime


total = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		day = datetime.datetime(year, month, 1).weekday()
		if day == 6:
			total += 1
print(total)