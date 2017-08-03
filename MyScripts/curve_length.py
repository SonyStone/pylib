import maya.cmds as cmds
from functools import partial

curves = cmds.ls( selection=True )

def arcLength(curve):
	cmds.setAttr(curve+'.arcLength', cmds.arclen( curve ))
	return

for curve in curves:
    cmds.addAttr(curve, longName='arcLength', attributeType='double')
    cmds.setAttr( curve+'.arcLength', keyable=True )
    cmds.scriptJob(event=["SelectionChanged", partial(arcLength, curve)] )