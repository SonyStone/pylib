L = [2 ** L for L in range(7)]
X = 5

if 2 ** X in L:
	print ('at index', L.index(2 ** X))
else:
	print(X, 'not found')