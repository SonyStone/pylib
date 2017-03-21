#list
a = [1,2,3,4,5]
a.append(100)
a.remove(4)
#print (a)
#tuple
a = (1,2,3,4)
#print (a)
#dict
#{key:value}
a= {
	1:True,
	2:False
}
#print (a)
#str
s1 = '\'string\''
s2 = "\"string\""

#print s1

a = 3 + 4 and 10 - 4 and "1"
#print a, type(a)

if 5 > 4:
	print 'Case 1'
else:
	print 'Case 2'

for a in range(10):
	if a == 3:
		continue
	print a,",", type(a)