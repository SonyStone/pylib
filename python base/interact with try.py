start = '''
Mark Lutz - Learning Python 5th edition
\tChapter 10, page 333
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
		num = int(reply)
	except:
		print('\'', reply, "\' is not digit")
	else:
		print(num ** 2)
print('Bye')