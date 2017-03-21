# keyRotation.py

import maya.cmds as cmds

def keyFullRotation( objectName, startTime, endTime, targetAttribute):
	cmds.cutKey( objectName, time=(startTime, endTime), attribute=targetAttribute)
	cmds.setKeyframe( objectName, time=startTime, attribute=targetAttribute, value=0 )
	cmds.setKeyframe( objectName, time= endTime, attribute=targetAttribute, value=360 )
	cmds.selectKey( objectName, time=(startTime, endTime), attribute=targetAttribute)
	cmds.keyTangent( inTangentType='linear', outTangentType='linear')


selectionList = cmds.ls( selection=True, type='transform' )

if len( selectionList ) >= 1:
	# print 'Selection items: %s' %( selectionList )
	startTime = cmds.playbackOptions( query=True, minTime=True )
	endTime = cmds.playbackOptions( query=True, maxTime=True )


	for objectName in selectionList:
		# objectTypeResult = cmds.objectType( objectName )
		# print '%s type: %s' %( objectName, objectTypeResult )
		keyFullRotation( objectName, startTime, endTime, 'rotateY')

else:
	print 'Please select at least one object'