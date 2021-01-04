nbres = 0
for a in range(201):
	for b in range(0, 201, 2):
		if a + b > 200:
			continue
		for c in range(0, 201, 5):
			if a + b + c > 200:
				continue
			for d in range(0, 201, 10):
				if a + b + c + d > 200:
					continue
				for e in range(0, 201, 20):
					if a + b + c + d + e > 200:
						continue
					for f in range(0, 201, 50):
						if a + b + c + d + e + f > 200:
							continue
						for g in range(0, 201, 100):
							if a + b + c + d + e + f + g > 200:
								continue
							for h in range(0, 201, 200):
								if a + b + c + d + e + f + g + h > 200:
									continue
								elif a + b + c + d + e + f + g + h == 200:
									nbres += 1
print(nbres)
