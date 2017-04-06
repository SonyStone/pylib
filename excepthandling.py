import maya.utils

def excepthook(tb_type, exc_object, tb, detail=2):
	return 'Hello!'
maya.utils.formatGuiException = excepthook
