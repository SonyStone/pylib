start = '''
Mark Lutz - Learning Python 5th edition
\tChapter 10, page 333
Supporting floating-point numbers
'''
doc = '''
Enter digits to power them
Enter \'stop\' to stop the programm
'''
print(start, doc)

while True:
	reply = input('Enter text:')
	if reply == 'stop':
		break
	try:
		print(float(reply) ** 2)
	except:
		print('Bad!' * 8)
print('Bye')