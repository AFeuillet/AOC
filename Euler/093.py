ops = ['+', '-', '*', '/']

maxi = 0

for a in range(1, 10):
	for b in range(a, 10):
		for c in range(b, 10):
			for d in range(c, 10):
				seta = [str(a), str(b), str(c), str(d)]
				tabi = set()
				for i in seta:
					for j in seta:
						if j == i:
							continue
						for k in seta:
							if k in [i, j]:
								continue
							for l in seta:
								if l in [i, j, k]:
									continue
								for op1 in ops:
									for op2 in ops:
										for op3 in ops:
											valtab = []
											valtab.append(eval(i + op1 + j + op2 + k + op3 + l))
											valtab.append(eval('(' + i + op1 + ' ' + j + ')' + op2  + '(' + k + ' ' + op3 + l + ')'))

											valtab.append(eval('(' + i + op1 + ' ' + j + ')' + op2  + ' ' + k + ' ' + op3 + l + ' '))
											valtab.append(eval('(' + i + op1 + ' ' + j + ' ' + op2  + ' ' + k + ')' + op3 + l + ' '))
											valtab.append(eval('((' + i + op1 + ' ' + j + ')' + op2  + ' ' + k + ')' + op3 + l + ' '))
								
											valtab.append(eval(' ' + i + op1 + ' ' + j + ' ' + op2  + '(' + k + ' ' + op3 + l + ')'))
											try:
												valtab.append(eval(' ' + i + op1 + '(' + j + ' ' + op2  + ' ' + k + ' ' + op3 + l + ')'))
											except ZeroDivisionError:
												pass
											try:
												valtab.append(eval(' ' + i + op1 + '(' + j + ' ' + op2  + '(' + k + ' ' + op3 + l + '))'))
											except ZeroDivisionError:
												pass

											valtab.append(eval(' ' + i + op1 + '(' + j + ' ' + op2  + ' ' + k + ')' + op3 + l + ' '))
											try:
												valtab.append(eval(' ' + i + op1 + '((' + j + ' ' + op2  + ' ' + k + ')' + op3 + l + ')'))
											except ZeroDivisionError:
												pass
											
											valtab.append(eval('(' + i + op1 + '(' + j + ' ' + op2  + ' ' + k + '))' + op3 + l + ' '))

											for vt in valtab:
												if isinstance(vt, int) and vt > 0:
													tabi.add(vt)
				old = 0
				for sat in sorted(tabi):
					if sat == old + 1:
						old = sat
					else:
						if old >= maxi:
							maxi = old
							print(seta, old)
						break
