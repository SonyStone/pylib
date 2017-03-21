import sys
import os

files = []
arg = sys.argv[1:]
# print arg
for a in arg:
	root = os.listdir(a)
	print root
	for f in root:
		if os.path.isfile(os.path.join(a, f)):
			if os.path.splitext(f)[-1] == '.txt':
				files.append(os.path.join(a, f))
		# print f
# print files

newName = raw_input('Enter name: ')
if newName:
	for i, f in enumerate(files):
		d = os.path.dirname(f)
		name, ext = os.path.splitext( os.path.basename(f))
		# print d, ' | ', name, ' | ', ext
		fName = newName + '_' + str(i + 1).zfill(3) + ext
		fullPath = os.path.join(d, fName)
		os.rename(f, fullPath)
		# print fullPath

raw_input()
