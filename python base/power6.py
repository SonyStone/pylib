L = [2 ** L for L in range(7)]
X = 5
powerX = 2 ** X

if powerX in L:
	print ('at index', L.index(powerX))
else:
	print(X, 'not found')