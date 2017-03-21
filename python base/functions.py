def mult2(x, m=True):
	if m:
		return x * 10
	else:
		return x / 10.0

print mult2(5, False)