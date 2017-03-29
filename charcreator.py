import pymel.core as pmc
import skeletonutils

def convert_hierarchies_main():
	"""'convert_hierarchies(pmc.selection())'.
	Prints and provides user feedback so only call from UI.
	"""

def convert_hierarchies(rootnodes):
	"""Calls 'convert_hierarchies' for each root node in 'rootnodes'
	(so passing in '[parent, child]' would convert the 'parent'
	hierarchy adduming 'child' lives under it).
	"""

def conver_hierarchy(node):
	"""Converts the hierarchy under and included 'rootnode'
	into joints tn the sane namespace as 'rootnode'.
	Deletes 'rootnode' and its hierarchy.
	Connections to nodes are not preserved on the newly
	created joints.
	"""
