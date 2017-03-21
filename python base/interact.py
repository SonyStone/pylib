start = '''
Mark Lutz - Learning Python 5th edition
\tChapter 10, page 332
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
	elif not reply.isdigit():
		print('\'', reply, "\' is not digit", sep='')
	else:
		print(int(reply) ** 2)
print('Bye')