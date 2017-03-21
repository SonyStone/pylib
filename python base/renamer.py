import sys
import os

# print sys.argv
arg = sys.argv[1:]

newName = raw_input('Enter name: ')
if newName:
	for i, f in enumerate(arg):
		d = os.path.dirname(f)
		name, ext = os.path.splitext( os.path.basename(f))
		# print d, ' | ', name, ' | ', ext
		fName = newName + '_' + str(i + 1).zfill(3) + ext
		fullPath = os.path.join(d, fName)
		os.rename(f, fullPath)
		# print fullPath

raw_input()
