start = '''
Mark Lutz - Learning Python 5th edition
\tChapter 10, page 335
Nesting Code Three Levels Deep
'''
doc = '''
Enter digits bigger then 20 to power them
Enter \'stop\' to stop the programm
'''
print(start, doc)

while True:
	reply = input('Enter text:')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print('Bad!' * 8)
	else:
		num = int(reply)
		if num < 20:
			print('low')
		else:
			print(num ** 2)
print('Bye')
input('Press \'Enter\' to exit')