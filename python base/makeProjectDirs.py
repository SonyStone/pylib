# python 2.7
import os
path = r'D:\1D\Python\python base'

folders = \
[ ['input', [
	['src', [] ],
	['doc', [] ],
	] ],
  ['output', [] ],
  ['scenes', [] ],
  ['assets', [
 	['textures', [] ],
 	['models', [
 		['characters', [] ],
 		['locations',  [] ],
 		] ],
 	] ]
]


def creatFolder(path):
	if not os.path.exists(path):
		os.mkdir(path)

def build(root, data):
	if root:
		creatFolder(root)
	if data:
		for d in data:
			name = d[0]
			path = os.path.join(root, name)
			creatFolder(path)
			# print path
			build(path, d[1])


projectname = raw_input('Enter project name: ')
if projectname:
	fullPath = os.path.join(path, projectname)
	build(fullPath, folders)
