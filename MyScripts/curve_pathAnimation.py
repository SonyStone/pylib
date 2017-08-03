import maya.cmds as cmds
from functools import partial

def arcLength(curve):
	cmds.setAttr(curve + '.arcLength', cmds.arclen( curve ))

def addArcLength(curve):
    cmds.addAttr(curve, longName='arcLength', attributeType='double')
    cmds.setAttr( curve + '.arcLength', keyable=True )
    crvInfoNode = cmds.createNode('curveInfo')
    cmds.connectAttr( curve + '.local', crvInfoNode + '.inputCurve', force=True)
    cmds.connectAttr( crvInfoNode + '.arcLength', curve + '.arcLength', force=True)
    return curve + '.arcLength'

def addPosition(obj):
    cmds.addAttr(obj, longName='position', attributeType='double')
    cmds.setAttr( obj +'.position', keyable=True )
    return obj + '.position'

path = cmds.ls('path*', selection=True)[0]
obj = cmds.ls('group*', selection=True)[0]

pathLenght = addArcLength(path)

cmds.pathAnimation(obj, fractionMode=True, follow=False, curve=path, name="motoion" + path )

pathAnimation = "motoion"+path

objPosition = addPosition(obj)


cmds.delete( pathAnimation + '_uValue')
cmds.expression(string= pathAnimation +".uValue = 1-((" + pathLenght + " - " + objPosition + ") / " + pathLenght + " );", uc='all')