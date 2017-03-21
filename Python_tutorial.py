#  PPPPPPPP                                                                     
#  PP     PP               t      hh                                            
#  PP  -   PP              tt     hh                                            
#  PP     PP  yy  -  yy tttttttt  hh hhhh     ooooooo   nn nnnnn  --------------
#  PPPPPPP     yy   yy     tt     hhh    hh  oo  -  oo  nnn    nn  -------------
#  PP      --   yy yy   -  tt  -  hh  -  hh  oo  -  oo  nn  -  nn  -------------
#  PP  -------   yyy   --  tt  -  hh  -  hh  oo  -  oo  nn  -  nn  -------------
#  PP  --------  yy   ---  tt  -  hh  -  hh  oo  -  oo  nn  -  nn  -------------
#  PP  -------  yy  -----  tt  -  hh  -  hh  oo  -  oo  nn  -  nn  -------------
#  PP  -----  yy   -------  tt    hh  -  hh   ooooooo   nn  -  nn  -------------

# <== коментарий
input('Press \'Enter\' to exit') 	# Задержка вывода консоли

"""> python -m idlelib.idle """ # запуск IDLE из командный строки для текущей папки
"""> cd 1D\Python\ """
# pip => python install packeges
"""
pip --proxy http://192.168.1.37:2718
pip install --proxy=http://192.168.1.37:2718 package
pip install --proxy=http://192.168.1.37:2718 xlwings	# exl 
python get-pip.py --proxy="http://192.168.1.37:2718"
"""
# Run Python versions
"""
C:\Python33\python
py
py -2
py -3.1
"""
# PART 1 Getting Started
	# Module Imports and Reloads
		import script1  				# one time import file
		reload(script1)					# reload scripts
		
		import imp
		imp.reload()
		
		from imp import reload
		reload(module)
		
		script1.X 						# > Spam!
		
		from script1 import X 			# recommend always using import instead of from
		X 								# > Spam!
		
		exec(open('script1').read()) 	# Run Module Files (код запущенного модуля вставляется в код, так он может перезаписать старые значения)
# PART 2 Types and Operations
	# CHAPTER 4 Introducing Python Object Types
		# Python's Core Data Types
			"""
			#Object type
			Numbers				1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
			Strings				'spam', "Bob's", b'a\x01c', u'sp\xc4m'
			Lists				[1, [2, 'three'], 4.5], list(range(10))
			Dictionaries		{'food': 'spam', 'taste': 'yum'}, dict(hours=10)
			Tuples				(1, 'spam', 4, 'U'), tuple('spam'), namedtuple
			Files				open('eggs.txt'), open(r'C:\ham.bin', 'wb')
			Sets				set('abc'), {'a', 'b', 'c'}
			Other core types	Booleans, types, None
			Program unit types	Functions, modules, classes
			Implementation-related types 	Compiled code, stack tracebacks
			"""
		# Numbers
			print(3.1415 * 2) 		# => 6.283
			123 + 222				# => 345
			1.5 * 4					# => 6.0
			2 ** 100 				# => 126765060022~~~
			len(str(2 ** 1000000))	# => 301030 How many digits in really BIG number
			
			import math
			math.pi 		# => 3.141592653589793
			math.sqrt(85) 	# => 9.219544457292887
			
			import random
			random.random()				# => 0.7335334012811705
			random.choice([1, 2, 3, 4]) # => 3
		# Strings
			# Sequence Operations
				S = 'Spam'
				len(S) 			# => 4
				S[0]			# => 'S'
				S[1]			# => 'p'
				S[-1]			# => 'm'
				S[len(S)-1]		# => 'm' Negative indexing, the hard way
				S[-2]			# => 'a'
				S[1:3]			# => 'pa'
				S[1:]			# => 'pam'	[1:len(S)]
				S[0:3]			# => 'Spa'
				S[:3]			# => 'Spa'	[0:3]
				S[:-1]			# => 'Spa'  [0:-1]
				S[:]			# => 'Spam' [0:len(S)]
				S + 'xyz'		# => 'Spamxyz' Concatenation
				S * 4 			# => 'SpamSpamSpamSpam' Repetition
			# Immutability
				S[0] = 'z'				# => Error
				S = 'z' + S[1:]
				S 						# => 'zpam'
				S.find('pa') 			# => 1
				S.replace('pa', 'XYZ') 	# => 'zXYZm'
				S 						# => 'zpam'
				
				line = 'aaa,bbb,ccccc,dd\n'
				line.split(',') 			# => ['aaa', 'bbb', 'ccccc', 'dd\n']
				line.rstrip()				# => 'aaa,bbb,ccccc,dd'
				line.rstrip().split(',') 	# => ['aaa', 'bbb', 'ccccc', 'dd']
				
				S.upper()		# => ZPAM
				S.isalpha()		# => True
				S.isdigit()		# => False
				
				S = 'shrubery'
				L = list(S)
				L 				# => ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
				L[1] = 'c'
				''.join(L) 		# => 'scrubbery'
				
				B = bytearray(b'spam')
				B.extend(b'eggs')
				B 				# => bytearray(b'spameggs')
				B.decode() 		# => 'spameggs'
			# Formatting
				'%s, eggs, and %s' % ('spam', 'SPAM!') 			# => 'spam, eggs, and SPAM!' #
				'{0}, eggs, and {1}'.format('spam', 'SPAM!') 	# => 'spam, '
				'{}, eggs, and {}'.format('sapm', 'SPAM!') 		# => 'spam, eggs, and SPAM!'
				# numeric reports
				'{:,.2f}'.format(296999.2567) 					# => '296,999.26' # Separators, decimal digits
				'%.2f | %+05d' % (3.14159, -42) 				# => '3.14 | -0042'
			# Getting Help
				dir(S)
				help(S.replace)
				help(S)
			# data type str, list, dict
			# Other Ways to Code Strings
				S = 'A\nB\tC'
				# \n is end-of-line
				# \t is tab
				len(S) 			# => 5 # Each stands for just one character
				ord('\n') 		# => 10 # binary value in ASCII
				S = 'A\0B\0C'
				len(S) 			# => 5
				S 				# => 'A\x00B\x00C' # Non-printables are displayed as \xNN hex escapes
	
				msg = """
				aaaaaaaaaaaaa
				bbb'''bbbbbbb""bbbbbb'bbb
				ccccccccccc
				"""
				msg 			# => '\aaaaaaaaaaaaa\nbbb\'\'\'bbbbbbb""bbbbbb\'bbb\nccccccccccc\n'
				
				# raw string literal
				r'C:\text\new'
			# Unicode Strings
				'sp\xc4m' 					# => 'spÄm' # normal str string are Unicode text
				b'a\xo1c' 					# => b'a\x01c' # bytes string are byte-based data
				u'sp\u00c4m' 				# => 'spÄm' # The 2.X Unicode literal works in 3.3+: just str
				
				'spam'.encode('utf8')		# => b'spam'
				'spam'.encode('utf16')		# => b'\xff\xfes\x00p\x00a\x00m\x00'
				'spam'.encode('ASCII')		# => b'spam'
				'sp\xc4\u00c4\U000000c4m' 	# => 'spÄÄÄm'
				
				'x' + b'y'.decode()
				'x'.encode() + b'y'	
			# Pattern Matching
				import re
				match = re.match('Hello[ \t]*(.*)world', 'Hello   Python world')
				match.group(1) 				# => 'Python '
				
				match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
				match.groups() 				# => ('usr', 'home', 'lumberjack')
				
				re.split('[/:]', '/usr/home:lumberjack') # => ['', 'usr', 'home', 'lumberjack']
				a = 0	
		# Lists
			# Sequence Operations
				L = [123, 'spam', 1.23]
				len(L) 			# => 3
				L[0] 			# => 123
				L[:-1] 			# => [123, 'spam']
				L = [4, 5, 6] 	# => [123, 'spam', 1.23, 4, 5, 6]
				L * 2 			# => [123, 'spam', 1.23, 123, 'spam', 1.23]
				L 				# => [123, 'spam', 1.23]
			# Type-Specific Operations
				L.append('NI')
				L 				# => [123, 'spam', 1.23, 'NI']
				L.pop(2) 		# => 1.23
				L 				# => [123, 'spam', 'NI']
				
				M = ['bb', 'aa', 'cc']
				M.sort()
				M 				# => ['aa', 'bb', 'cc']
				M.reverse()
				M 				# => ['cc', 'bb', 'aa']
	
			# Nesting
				M = [[1, 2, 3],
					 [4, 5, 6],
					 [7, 8, 9]]
				M 				# => [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
				M[1] 			# => [4, 5, 6]
				M[1][2] 		# => 6
	
			# Comprehensions
				col2 = [row[1] for row in M] # Collect the items in column 2
				col2 			# => [2, 5, 8]
				[row[1] + 1 for row in M] # => [3, 6, 9] # Add 1 to each item in column 2
				[row[1] for row in M if row[1] % 2 == 0] # => [2, 8] # Filter out odd items
				diag = [M[i][i] for i in [0, 1, 2]] # Collect a diagonal from matrix
				diag 			# => [1, 5, 9]
				doubles = [c * 2 for c in 'spam'] # => Reapeat characters in string
				doubles 		# => ['ss', 'pp', 'aa', 'mm']
				
				list(range(4)) # => [0, 1, 2, 3]
				list(range(-6, 7, 2)) # => [-6, -4, -2, 0, 2, 4, 6]
	
				[[x ** 2, x ** 3] for x in range(4)] # => [[0, 0], [1, 1], [4, 8], [9, 27]]
				[[x, x /2, x * 2] for x in range(-6, 7, 2) if x > 0] # => [[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]
				
				G = (sum(row) for row in M) # Create a generator of row sums
				next(G) 		# => 6
				next(G) 		# => 15 # Run the iteration prorocol next()
				
				list(map(sum, M)) # => [6, 15, 24] # Map sum over items in M
		# Dictionaries
			# Mapping Operations
				D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
				D['food'] 		# => 'Spam'
				D['quantity'] += 1 # add 1 to 'quantity' value
				D 				# => {'color': 'pink', 'food': 'Spam', 'quantity': 5}
				
				D = {}
				D['name'] = 'Bob'
				D['job'] = 'dev'
				D['age'] = 40
				D 				# => {'name': 'Bob', 'age': 40, 'job': 'dev'}
				print(D['name']) # => Bob
				
				bob1 = dict(name='Bob', job='dev', age=40)
				bob1 			# => {'name': 'Bob', 'age': 40, 'job': 'dev'}
				
				bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping
				bob2 			# => {'name': 'Bob', 'age': 40, 'job': 'dev'}

			# Nesting Revisited
				rec = {'name':{'first': 'Bob', 'last': 'Smith'},
					   'jobs': ['dev', 'mgr'],
					   'age' : 40.5}
				
				rec['name'] 			# => {'last': 'Smith', 'first': 'Bob'}
				rec['name']['last'] 	# => 'Smith'
				rec['jobs'] 			# => ['dev', 'mgr']
				rec['jobs'][-1] 		# => 'mgr'
				rec['jobs'].append('janitor')
				rec 					# => {'jobs': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}

			# Sorting Keys:for loops
				D = {'a': 1, 'b':2, 'c':3}
				D 				# => {'b': 2, 'c': 3, 'a': 1}
				
				Ks = list(D.keys())
				Ks 				# => ['b', 'c', 'a']
				
				Ks.sort()
				Ks 				# => ['a', 'b', 'c']
				
				for key in Ks:
					print(key, '=>', D[key]) # =>	a => 1
											 # 		b => 2
											 #		c => 3
				
				for key in sorted(D):
					print(key, '=>', D[key]) # =>	a => 1
											 # 		b => 2
											 #		c => 3	
		# Tuples
			T = (1, 2, 3, 4)
			len(T) 			# => 4
			T + (5, 6) 		# => (1, 2, 3, 4, 5, 6)
			T[0] 			# => 1
			T.index(4) 		# => 3
			T.count(4) 		# => 1
			T[0] = 2 		# => ...error...
			T = (2, ) + T[1:]
			T 				# => (2, 2, 3, 4)
		# Files
			f = open('data.txt', 'w')
			f.write('Hello\n') # => 6
			f.write('world\n') # => 6
			F.close()
			
			# Binary Bytes Files
				import struct
				packed = struct.pack('>i4sh', 7, b'spam', 8)
				packed 			# => b'\x00\x00\x00\x07spam\x00\x08'
				file = open('data.bin', 'wb')
				file.write(packed) # => 10
				file.close()
				data = open('data.bin', 'rb').read()
				data 			# => b'\x00\x00\x00\x07spma\x00\x08'
				data[4:8] 		# => b'spma'
				list(data) 		# => [0, 0, 0, 7, 115, 112, 109, 97, 0, 8]
				struct.unpack('>i4sh', data) # => (7, b'spma', 8)
			
			# Unicode Text Files
				S = 'sp\xc4m'
				S 				# => 'spÄm'
				S[2] 			# => 'Ä'
				file = open('unidata.txt', 'w', encoding='utf-8')
				file.write(S) 	# => 4
				file.close()
				text = open('unidata.txt',encoding='utf-8').read()
				text 			# => 'spÄm'
				len(text) 		# => 4
		# Other Core Types
			import decimal
			d = decimal.Decimal('3.141')
			d + 1 			# => Decimal('4.141')
			
			from fractions import Fraction
			f = Fraction(2, 3)
			f + 1 			# => Fraction(5, 3)
			
			1 > 2, 1 < 2 	# => (False, True)
			bool('spam') 	# => True

			# User-Defined Classes
				class Worker:
					def __init__(self, name, pay):
						self.name = name
						self.pay = pay
					def lastName(self):
						return self.name.split()[-1]
					def giveRaise(self, percent):
						self.pay *= (1.0 + percent)
				
				bob = Worker('Bob Smith', 50000)
				sue = Worker('Sue Jones', 60000)
				bob.lastName() 		# => 'Smith'
				sue.lastName() 		# => 'Jones'
				sue.giveRaise(.1)
				sue.pay 			# => 66000.0
	# CHAPTER 5 Numeric Types
		# Numeric Type Basics
			# Python Expression Operators
				yield x 				# Generator function send protocol
				lambda args: expression	# Anonymous function generation
				x if y else z 			# Ternary selection (x is evaluted only if y is true)
				x or y 					# Logical OR (y is evaluted only if x if false)
				x and y 				# Logical AND (y is evaluted only)
				not x 					# Logical negation
				x in y,x not in y 		# Membership (iterables, sets)
				x is y, x is not y 		# Object identity tests
				x < y, x <= y, x > y, x >= y # Magnitude comparison, set subset and superset;
				x == y, x != y 			# Value equality ooperators
				x | y 					# Bitwise OR, set union
				x ^ y 					# Bitwise XOR, set symmetric difference
				x & y 					# Bitwise AND, set intersection
				x << y, x >> y 			# Shift x left or right by y bits
				x + y 					# Addition, concatenation
				x - y 					# Subtraction, set difference
				x * y 					# Multilication, repetition
				x % y 					# Remainder, format
				x / y, x // y 			# Division: true and floor
				-x, +x 					# Negation, identity
				~x 						# Bitwise NOT (inversion)
				x ** y 					# Power (exponentiation)
				x[i]					# Indexing (sequence, mapping, others)
				x[i:j:k]				# Slicing
				x(...) 					# Call (function, method, calss, other callable)
				a.attr 					# Attribute reference
				(...) 					# Tulpe, expression, generator expression
				[...] 					# List, list comprehension
				{...}					# Dictionary, set, set and dictionary comprehensions
		# Numbers in Action
			# Comparisons: Normal and Chained
				1.1 + 2.2 == 3.3 			# => False
				1.1 + 2.2 					# => 3.3000000000000003
				int(1.1 + 2.2) == int(3.3) 	# => True
			# Floor versus truncation
				import math
				math.floor(2.5) 		# => 2
				math.floot(-2.5) 		# => -3
				math.trunc(2.5) 		# => 2
				math.trunc(-2.5) 		# => -2
			# Complex Numbers
				1j * 1J 				# => (-1+0j)
				2 + 1j * 3 				# => (2+3j)
			# Hex, Octal, Binary: Literals and Conversions
				oct(64), hex(64), bin(64) 					# => ('0o100', '0x40', '0b1000000')
				64, 0o100, 0x40, 0b1000000 					# => (64, 64, 64, 64)
				int('64'), int('100', 8), int('40', 16), int('1000000', 2) # => (64, 64, 64, 64)
				int('0x40', 16), int('0b1000000', 2) 		# => (64, 64)
				eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000') # => (64, 64, 64, 64)
				'{0:o}, {1:x}, {2:b}'.format(64, 64, 64) 	# => '100, 40, 1000000'
				'%o, %x, %x, %X' % (64, 64, 255, 255) 		# => '100, 40, ff, FF'
			# Other Built-in Numeric Tools
				import math
				math.pi, math.e 							# =>(3.141592653589793, 2.718281828459045)
				math.sin(2 * math.pi / 180) 				# => 0.03489949670250097
				math.sqrt(144), math.sqrt(2) 				# => (12.0, 1.4142135623730951)
				pow(2, 4), 2 ** 4, 2.0 ** 4.0 				# => (16, 16, 16.0)
				min(3, 1, 2, 4), max(3, 1, 2, 4) 			# => (1, 4)
				
				math.floor(2.567), math.floor(-2.567) 		# => (2, -3)
				math.trunc(2.567), math.trunc(-2.567) 		# => (2, -2)
				int(2.567), int(-2.567) 					# => (2, -2)
				round(2.567), round(2.467), round(2.567, 2) # => (3, 2, 2.57)
				'%.1f' % 2.567, '{0:.2f}'.format(2.567) 	# => ('2.6', '2.57')
				
				import random
				random.random() 							# => 0.9726485651691155
				random.randint(1, 10) 						# => 1
				random.choice(['life of Brian', 'Holy Grail', 'Meaning of Life']) # => 'Holy Grail'
				
				suits = ['hearts', 'clubs', 'diamonds', 'spades']
				random.shuffle(suits)
				suits 					# => ['clubs', 'diamonds', 'hearts', 'spades']
		# Other Numeric Types
			# Decimal Type
				# Decimal basics
				0.1 + 0.1 +0.1 - 0.3 	# => 5.551115123125783e-17
				Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # => Decimal('0.0')
			# Fraction Type
				# Fraction basics
				from fractions import Fraction
				x = Fraction(1, 3)
				y = Fraction(4, 6)
				x, y 						# => (Fraction(1, 3), Fraction(2, 3))
				print(x, y) 				# => 1/3 2/3
				print(x + y, x - y, x * y) 	# => 1 -1/3 2/9
				Fraction('.25') 			# => Fraction(1, 4)
			# Sets
				engineers = {'bob', 'sue', 'ann', 'vic'}
				managers = {'tom', 'sue'}
				'bob' in engineers 					# => True
				engineers & managers 				# => {'sue'}
				engineers | managers 				# => {'bob', 'sue', 'ann', 'vic', 'tom'}
				engineers - managers 				# => {'vic', 'bob', 'ann'}
				managers - engineers 				# => {'tom'}
				engineers > managers 				# => False
				{'bob', 'sue'} < engineers 			# =>True
				(managers | engineers) > managers 	# => True
				managers ^ engineers 				# => {'vic', 'bob', 'ann', 'tom'}
				(managers | engineers) - (managers ^ engineers) # => {'sue'}
		# Booleans O_o
			type(True) 				# => <class 'bool'>
			isinstance(True, int) 	# => True
			True == 1 				# => True
			True is 1 				# => False
			True or False 			# => True
			True + 4 				# => 5
	# CHAPTER 6 The Dynamic Typing Interlude
	# CHAPTER 7 String Fundamentals
		# String Basics
			S = ''					# Empty string
			S = "spam's" 			# Double quotes, same as single
			S = 's\np\ta\x00m' 		# Escape sequences
			S = """...multiline..."""	# Triple-quoted block string
			S = r'\temp\spam'		# Raw string (no escapes)
			B = b'sp\xc4m'			# Byte strings
			U = u'sp\u00c4m'		# Unicdoe strings
			S1 + S2, S * 3			# Concatenate, repeat
			S[i], S[i:j], len(S)	# Index, slice, length
			"a %s parrot" % kind 	# String formatting учзкуыышщт
			"a {0} parrot".format(kind) # String formatting method
			S.find('pa') 			# String methods: search
			S.rstrip() 				# remove whitespace
			S.replace('pa', 'xx') 	# replacement
			S.split(',') 			# split on delimiter
			S.isdigit() 			# content test
			S.lower() 				# case conversion
			S.endswith('spam')		# end test
			'spam'.join(strlist)	# delimiter join
			S.encode('latin-1') 	# Unicode encoding
			B.decode('utf8')		# Unicode decoding
			for x in S: print(x)	# Iteration, membership
			'spam' in S
			[c * 2 for c in S]
			map(ord, S)
			re.match('sp(.*)am', line)	# Pattern matching: library module
		# String Literals
			# Escape Sequences Represent Special Characters
				# String backslash characters # Like in C, C++ and other
				"\newline" 				# Ignored (continuation line)
				"\\"					# Backslash (stores one \)
				"\'" 					
				"\""				
				"\a"					# Bell
				"\b"					# Backspace
				"\f"					# Formfeed
				"\n"					# Newline (linefeed)
				"\r"					# Carriage return
				"\t"					# Horizontal tab
				"\v"					# Vertical tab
				"\xhh"					# Cgaracter with hex value hh (exactly 2 digits)
				"\ooo"					# Character with octal value ooo (up to 3 digits)
				"\0"					# Null: binary 0 character (doesn't end string)
				"\N{ id }" 				# Unicode database ID
				"\uhhh"					# Unicode character with 16-bit hex value
				"\Uhhhhhh"				# Unicode character with 32-bit hex value
				"\other"				# Not an escape (keeps both \ and other)
		# Strings in Action
			# Changing Strings
				S = 'spam'
				S[0] = 'x'				# => TypeError # Raises an error!
				
				S = S + 'SPAM!'  		# To change a string, make a new one
				S 						# => 'spamSPAM!'
				S = S[:4] + 'Burger' + S[-1]
				S 						# => 'sapmBurger!'
				
				S = 'splot'
				S = S.replace('pl', 'pamal')
				S 						# => 'spamalot'
		# String Methods
			str = 'String Methods'
			str.capitalize() 		# => 'String methods'
			str.casefold() 			# => 'string methods'
			str.center(30, '-') 	# => '--------String Methods--------'
			str.count('t',0,-1) 	# => 2 # (sub[,start[,end]])
		# String Formatting Expressions
			'My {1[king]} runs {0.platform}'.format(sys, {'king': 'laptop'}) # => 'My laptop runs win32'
			'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}) # => 'My laptop runs win32'
	# CHAPTER 8 Lists and Dictionates
		# Lists
			L = [] 								# An empty list
			L = [123, 'abc', 1.23, {}] 			# Four items: indexes 0..3
			L = ['Bob', 40.0, ['dev', 'mgr']] 	# Nested sublists
			L = list('spam') 					# List of an iterable's items
			L = list(range(-4, 4)) 				# list of successive integers
			L[i] 								# Index
			L[i][j] 							# Index of index
			L[i:j] 								# slice
			len(L) 								# length
			L1 + L2 							# Concatenate
			L * 3 								# repeat
			for x in L: print(x)				# Iteration
			3 in L 								# membership
			L.append(4)							# Methods: growing
			L.extend([5,6,7])
			L.insert(i, X)
			L.index(X)							# Methods: searching
			L.count(X)
			L.sort() 							# Methods: sorting, reversing
			L.reverse()
			L.copy()
			L.clear()
			L.pop(i) 							# Methods, statements: shrinking
			L.remove(X)
			del L[i]
			del L[i:j]
			L[i:j] = []
			L[i] = 3 							# Index assignment, slice assignment
			L[i:j] = [4,5,6]
			L = [x**2 for x in range(5)] 		# List comprehensions and maps
			List(map(ord, 'spam'))
		# Dictionares
			D = {}								# Empty dictionary
			D = {'name': 'Bob', 'age': 40}		# Two-item dictionary
			E = {'cto': {'name': 'Bob', 'age': 40}} # Nesting
			D = dict(name='Bob', age=40) 		# Alternative construction techniques:
			D = dict([('name', 'Bob'), ('age', 40)]) # keywords, key/value pairs, zipped key/value pairs, key lists
			D = dict(zip(keyslist, valueslist))
			D = dict.fromkeys(['name', 'age'])
			D['name'] 							# Indexing by key
			E['cto']['age']
			'age' in D  						# Membership: key present test
			D.keys() 							# Methods: all keys,
			D.values() 							# all values,
			D.items() 							# all key+value tuples,
			D.copy() 							# copy (top-level),
			D.clear() 							# clear (remove all items),
			D.update(D2) 						# merge by keys,
			D.get(key, default?) 				# fetch by key, if absent default (or None),
			D.pop(key, default?) 				# remove by key, if absent default (or error)
			D.setdefault(key, default?) 		# fetch by key, if absent set default (or None),
			D.popitem() 						# remove/return any (key, value) pair; etc.
			len(D) 								# Length: number of stored entries
			D[key] = 42 						# Adding/changing keys
			del D[key] 							# Deleting entries by key
			list(D.keys()) 						# Dictionary views (Python 3.X)
			D1.keys() & D2.keys()
			D.viewkeys(), D.viewvalues() 		# Dictionary views (Python 2.7)
			D = {x: x*2 for x in range(10)} 	# Dictionary comprehensions (Python 3.X, 2.7)
	# CHAPTER 9 Tuples, Files, and Everything Else
		# Tuples
			()									# AN empty tuple
			T = (0,)							# A one-item tuple (not an expression)
			T = (0, 'Ni', 1.2, 3) 				# A four-item tuple
			T = 0, 'Ni', 1.2, 3 				# Another four-item tuple (same as prior line)
			T = ('Bob', ('dev', 'mgr')) 		# Nested tuples
			T = tuple('spam') 					# Tuple of items in an iterable
			T[i] 								# Index, 
			T[i][j] 							# index of index, 
			T[i:j] 								# slice, 
			len(T) 								# length
			T1 + T2 							# Concatenate
			T * 3 								# repeat
			for x in T: print(x) 				# Iteration, membership
			'spam' in T
			[x ** 2 for x in T]
			T.index('Ni') 						# Methods in 2.6, 2.7, and 3.X: search, count
			T.count('Ni')
			namedtuple('Emp', ['name', 'jobs']) # Named tuple extension type
		# Files
			output = open(r'C:\spam', 'w') 		# Create output file ('w' means write)
			input = open('data', 'r') 			# Create input file ('r' means read)
			input = open('data')
			open('testjson.txt',, encoding='utf-8')				# Same as prior line ('r' is the default)
			aString = input.read() 				# Read entire file into a single string
			aString = input.read(N) 			# Read up to next N characters (or bytes) into a string
			aString = input.readline() 			# Read next line (including \n newline) into a string
			aList = input.readlines() 			# Read entire file into list of line strings (with \n)
			output.write(aString) 				# Write a string of characters (or bytes) into file
			output.writelines(aList) 			# Write all line strings in a list into file
			output.close() 						# Manual close (done for you when file is collected)
			output.flush() 						# Flush output buffer to disk without closing
			anyFile.seek(N) 					# Change file position to offset N for next operation
			for line in open('data'): 			# use line File iterators read line by line
			open('f.txt', encoding='latin-1') 	# Python 3.X Unicode text files (str strings)
			open('f.bin', 'rb') 				# Python 3.X bytes files (bytes strings)
			codecs.open('f.txt', encoding='utf8') # Python 2.X Unicode text files (unicode strings)
			open('f.bin', 'rb') 				# Python 2.X bytes files (str strings)
# PART 3 Statements and Syntax
	# CHAPTER 10 Introducing Python Statements
		# Python statements
		
		# \/ Example				# \/ Statement 					# \/ Role
		a, b = 'good', 'bad'		# Assignment 					# Creating references
		
		log.write("spam, ham") 		# Calls and other expressions 	# Running functions
		print('The Killer', joke) 	# print calls 					# Printing objects
		
		if "python" in text:		# if/elif/else					# Selecting actions
			print(text)
		
		for x in mylist:			# for/else						# Iteration
			print(x)
		
		while X > Y:				# while/else					# General loops
			print('hello')
		
		while True:					# pass							# Empty placeholder
			pass
		
		while True:					# break							# Loop exit
			if exittest(): break
		
		while True:					# continue						# Loop continue
			if skiptest(): continue
		
		def f(a, b, c=1, *d):		# def 							# Functions and methods
			print(a+b+c+d[0])
		
		def f(a, b, c=1, *d):		# return						# Functions results
			return a+b+c+d[0]
		
		def gen(n):					# yield							# Generator functions
			for i in n: yield i*2
		
		x = 'old'					# global						# Namespaces
		def function():
			global x, y; x = 'new'
		def outer():				# nonlocal						# Namespaces (3.X)
			x = 'old'
			def function():
				nonlocal x; x = 'new'
		import sys					# import 						# Module access
		from sys import stdim 		# from 							# Attribute access
		class Subclass(Superclass):	# class 						# Building objects
			staticData = []
			def method(self): pass
		try:						# try/except/finally 			# Catching exceptions
			action()
		except:
			print('action error')
		raise EndSearch(location)	# raise 						# Triggering exceptions
		assert X > Y, 'X too small'	# assert 						# Debugging checks
		with open('data') as myfile:# with/as 						# Context managers
			process(myfile)
		del data[k]					# del 							# Deleting references
		del data[i:j]
		del obj.attr
		del variable
	# CHAPTER 11 Assignments, Expressions, and Prints
		# Assignment statement forms
		spam = 'Spam' 					# Basic form
		spam, ham = 'yum', 'YUM' 		# Tuple assignment (positional)
		[spam, ham] = ['yum', 'YUM'] 	# List assignment (positional)
		a, b, c, d = 'spam'				# Sequence assignment, generalized
		a, *b = 'spam' 					# Extended sequence unpacking (Python 3.X)
		spam = ham = 'lunch'			# Multiple-target assignment
		spams += 42 					# Augmented assignment (equivalent to spams = spams + 42)
		
		# Augmented assignment statements
		X += Y, X &= Y, X -= Y, X |= Y
		X *= Y, X ^= Y, X /= Y, X >>=Y
		X %= Y, X <<=Y, X **=Y, X //=Y
		
		# Python reserved words
		False;		class;		finally;	is;			return;
		None;		continue;	for;		lambda;		try;
		True;		def;		from;		nonlocal;	while;
		and;		del;		global;		not;		with;
		as;			elif;		if;			or;			yield;
		assert;		else;		import;		pass;
		break;		except;		in;			raise;
		
		# Common Python expression statements
		spam(eggs, ham) 		# Function calls
		spam.ham(eggs) 			# Method calls
		spam 					# Printing variables in the interactive interpreter
		print(a, b, c, sep='') 	# Printing operations in Python 3.X
		yield x ** 2 			# Yielding expression statements
		
		# Printing, the hard way
		import sys
		sys.stdout.write('hello world\n') 	# => hello world
		sys.stdout =  open('log.txt', 'a') 	# Redirects prints to a file
		...
		print(x, y, x) 						# Shows up in log.txt
		
		log = open('log.txt', 'a') 			# 3.X
		print(x, y, z, file=log)			# Print to a file-like object
	# CHAPTER 12 if Tests and Syntax Rules
		# if Tests and Syntax Rules
		if test1:		# if test
			statements1	# Associated block
		elif test2:		# Optional elifs
			statements2
		else:			# Optio
			statements3
		
		# Loops
		while test:		# Loop test
			statements 	# Loop body
		else:			# Optional else
			statements 	# Run if didn't exit loop with break
		
		break 			# Jumps out of the closest enclosing loop (past the entire loop statement)
		continue 		# Jumps to the top of the closest enclosing loop (to the loop's header line)
		pass			# Does nothing at all: it's an empty statement placeholder
		... 			# Alternative to pass
		Loop else block # Runs if and only if the loop is exited normally (without hitting a break)
	# CHAPTER 13 while and for Loops
		# while Loops
		while :
			statements
			if test: break 		# Exit loop now, skip else if present
			if test: continue 	# Go to top of loop now, to test1
		else:
			statements 			# Run if we didn't hit a 'break'
		
		# for Loops
		for target in object:	# Assign object items to target
			statements 			# Repeated loop body: use target
		else: 					# Optional else part
			statements 			# If we didn't hit a 'break'
		
		[a for a in dir(list) if not a.startswith('__')]
		[x for x in ['spam', '', 'ni'] if bool(x)]
		[x for x in ['spam', '', 'ni'] if x]
		# Parallel Traversals: zip and map
		L1 = [1,2,3,4]
		L2 = [5,6,7,8]
		zip(L1, L2) # => <zip object at 0x026523C8>
		list(zip(L1, L2)) # => [(1, 5), (2, 6), (3, 7), (4, 8)] # list() required in 3.X, not 2.X
	# CHAPTER 14 Iterations and Comprehensions
		# iteration
		L = [1, 2, 3, 4, 5]
		
		for i in range(len(L)):
			L[i] += 10
		L # => [11, 12, 13, 14, 15]
		
		L = [x + 10 for x in L]
		L # => [21, 22, 23, 24, 25]
		
		
		[x + y for x in 'abc' for y in 'lmn']
		# => ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
		res = []
		for x in 'abc':
			for y in 'lmn':
				res.append(x + y)
		res
		# => ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
		''' need to learn more'''
	# CHAPTER 15 The Documentation Interlude
		# Documentation
		# Python documentation sources
		# comments					# In-file documentation
		'The dir function 			'# Lists of attributes available in objects
		'Docstrings:__doc__ 		'# In-file documentation attached to objects
		'PyDoc: the help function 	'# Interactive help for objects
		'PyDocy: HTML reports 		'# Module documentation in a browser
		'Sphinx third-party tool 	'# Richer documentation for larger projects
		'The standart manual set 	'# Official language and library descriptions
		'Web resources 				'# Online tutorials, examples, and so on
		'Published books 			'# Commercially polished reference texts
		
		# PyDoc
		"""
		c:\code>
		python -m pydoc -b
		py -3 -m pydoc -b
		C:\python33\python -m pydoc -b
		"""# => Server ready at http://localhost:62135
# PART 4 Functions and Generators
	# CHAPTER 16 Function Basics
		# Examples 									# Statement or expression
		myfunc('spam', 'eggs', meat=ham, *rest) 	# Call expressions
		
		def printer(message): 						# def
			print('Hello ' + str(message))
		
		def adder(a, b=1, *c): 						# return
			return a + b + c[0]
		
		x = 'old' 									# global
		def changer():
			global x; x = 'new'
		
		def outer(): 								# nonlocal (3.X)
			x = 'old'
			def changer():
				nonlocal x; x = 'new'
		
		def squares(x): 							# yield
			for i in range(x): yield i ** 2
		
		funcs = [lambda x: x**2, lambda x: x**3]	# lambda
		
		
		# def Statements
		
		def name(arg1, arg2, ... argN):
			statements
			...
			return value
		
		for x in xrange(1,10):
			pass
		
		# def Executes at Runtime
		
		if test:
			def func():	# Define func this way
				...
		else:
			def func():	# Or else this way
				...
		...
		func()			# Call the version selected and built
		
		othername = func 	# Assign function object
		othername() 		# Call func again
		
		def func(): ... 	# Create function object
		func() 				# Call object
		func.attr = value 	# Attach attributes
		
		#Definition
		def intersect(seq1, seq2):
			res = []				# Start empty
			for x in seq1:			# Scan seq1
				if x in seq2:		# Common item?
					res.append(x)	# Add to end
			return res
		
		s1 = "SPAM"
		s2 = "SCAM"
		intersect(s1, s2) 			# String 
		# => ['S', 'A', 'M']
		[x for x in s1 if x in s2] 	
		# => ['S', 'A', 'M']
		
		x = intersect([1, 2, 3], (1, 4))  # Mixed types
		x 	# Saved result object
		# => [1]
	# CHAPTER 17 Scopes
		# Python Scope Basics
			X = 99		# Global (module) scope X
			def func():
				X = 88 	# Local (function) scope X: a different variable
			
			# Name Resolution: The LEGB Rule
			"""
			Built-in (Python)
				Names preassigned in the built-in names modules: open, range,
				SyntaxError...
			
				Global (module)
					Names assigned at the top-level of module file, or declared
					globla in a def within the file.
			
					Enclosing function locals
						Names in the local scope of any and all enclosing functions
						(def or lambda), from inner to outer.
			
						Local (function)
							Names assigned in any way within a function (def
							or lambda), and not declared global in that function.
			"""
			# Scope Example
			# Global scope
			X = 99 			# X and func assigned in module: global
			def func(Y): 	# Y and Z assigned in function: locals
				# Local scope
				Z = X + Y 	# X is a global
				return Z
			func(1) 		# func in module: result=100	
		# The global Statement
			X = 88 			# Global X
			def func():
				global X
				X = 99		# Global X: outside def
			func()
			print(X) 		# Prints 99
			
			y, z = 1, 2 	# Global variables in module
			def all_global():
				global x 	# Declare globals assigned
				x = y + z 	# No need to declare y, z: LEGB rule
			
			# Other Ways to Access Globals
			# thismod.py
			var = 99
			def local():
				var = 0 	# Change local var
			
			def glob1():
				global var 	# Declare global (normal)
				var += 1	# Change global var
			
			def glob2():
				var = 0				# Change local var
				import thismod 		# Import myself
				thismod.var += 1 	# Change global var
			
			def glob3():
				var = 0							# Change local var
				import sys						# Import system table
				glob = sys.modules['thismod']	# Get module object (or use __name__)
				glob.var += 1					# Change global var
			
			def test():
				print(var)
				local(); glob1(); glob2(); glob3()
				print(var)
		
			# consol
			import thismod
			thismod.test() # => 99 102
			thismod.var # => 102
		# Scopes and Nested Functions
		# Function factory (a.k.a. closures)
			# A simple function factory
			def maker(N):
				def action(X):
					return X ** N 	# Make and return action
				return action 		# action retains N from enclosing
			
			f = maker(2)
			g = maker(3) 			# g remembers 3, f remembers 2
			g(4)	# => 64			# 4 ** 3
			f(4)	# => 16			# 4 ** 2
			
			def maker(N):
				return lambda X: X ** N # lambda functions retain state too
			
			# Retaining Enclosing Scope State with Defaults
			def f1():
				x = 88
				def f2(x=x): 		# Remember enclosing scope X with defaults
					print(x)
				f2()
			
			f1() 	# => 88
			
			def f1():
				x = 88
				f2(x)
			
			def f2(x):
				print(x)
			
			f1() 	# => 88
		# The nonlocal Statement in 3.X
			# nonlocal Basics
			nonlocal # skip my local scope entirely
	# CHAPTER 18 Arguments
		# Argument-Passing Basics
		# Special Argument-Mathching Modes
			# Argument Matching Syntax
			# Syntax 				# Location 	# Interpretation
			func(value)				# Caller	# Normal argument: matched by position
			func(name=value)		# Caller	# Keyword argument: matched by name
			func(*iterable)			# Caller	# Pass all objects in iterable as individual positional arguments
			func(**dict)			# Caller 	# Pass all key/value pairs in dict as individual keyword arguments
			def func(name):			# Function 	# Normal argument: matches any passed value by position or name
			def func(name=value):	# Function 	# Default argument value, if not passed in the call
			def func(*name):		# Function 	# Matches and collects remaining positional arguments in a tuple
			def func(**name):		# Function 	# Matches and collects remaining keyword arguments in a dictionary
			def func(*other, name):	# Function 	# Arguments that must be passed by keyword only in calls (3.X)
			def func(*, name=value):# Function 	# Arguments that must be passed by keyword only in calls (3.X)
			# Combining keywords and defaults
			def func(spam, eggs, toast=0, ham=0):
				print((spam, eggs, toasr, ham))
			
			func(1, 2)						# => (1, 2, 0, 0)
			func(1, ham=1, eggs=0)			# => (1, 0, 0, 1)
			func(spam=1, eggs=0)			# => (1, 0, 0, 0)
			func(toast=1, eggs=2, spam=3)	# => (3, 2, 1, 0)
			func(1, 2, 3, 4)				# => (1, 2, 3, 4)
			
			# Arbitrary Arguments Examples
			# Headers: Collections aruments
			def f(a, *pargs, **kargs): print(a, pargs, kargs)
			f(1, 2, 3, 4, x=5, y=6) 	# => 1 (2, 3, 4) {'y': 6, 'x': 5}


# ┌──────────────────────────────────────────┐
# │ Learning Python 5E -- 546 (598 /1594)    │
# ├──────────────────────────────────────────┤
# │ Изучаем Python 4E -- (463 / 1280)        │
# └──────────────────────────────────────────┘
