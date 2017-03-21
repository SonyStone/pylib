# keyRotationWithUI.py
import maya.cmds as cmds
import functools

def createUI( windowTitle, applyCallback, clearAnimationCallback ):
	windowID = 'myWindowID'

	if cmds.window( windowID, exists=True ):
		cmds.deleteUI( windowID )

	cmds.window( windowID, title=windowTitle, sizeable=False, resizeToFitChildren=True )

	cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[(1,75), (2,60), (3,60)], columnOffset=[(1,'right',3)] )
	
	cmds.text( label='Time Range:' )
	startTimeField = cmds.intField( value=cmds.playbackOptions( q=True, minTime=True ))
	endTimeField = cmds.intField( value=cmds.playbackOptions( q=True, maxTime=True ))

	cmds.text( label='Attribute:' )
	targetAttributeField = cmds.textField( text='rotateY' )
	cmds.separator( h=10, style='none' )

	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )
	cmds.separator( h=10, style='none' )

	cmds.button( label='Clear', command=functools.partial( clearAnimationCallback,
													startTimeField,
													endTimeField) )
	cmds.button( label='Apply', command=functools.partial( applyCallback,
													startTimeField,
													endTimeField,
													targetAttributeField ) )
	def cancelCallback( *args ):
		if cmds.window( windowID, exists=True ):
			cmds.deleteUI( windowID )
	cmds.button( label='Cancel', command=cancelCallback )

	cmds.showWindow()

def keyFullRotation( objectName, startTime, endTime, targetAttribute):
	cmds.cutKey( objectName, time=(startTime, endTime), attribute=targetAttribute)
	cmds.setKeyframe( objectName, time=startTime, attribute=targetAttribute, value=0 )
	cmds.setKeyframe( objectName, time= endTime, attribute=targetAttribute, value=360 )
	cmds.selectKey( objectName, time=(startTime, endTime), attribute=targetAttribute)
	cmds.keyTangent( inTangentType='linear', outTangentType='linear')

def clearAnimationCallback( startTimeField, endTimeField, *args ):

	startTime = cmds.intField( startTimeField, query=True, value=True )
	endTime = cmds.intField( endTimeField, query=True, value=True )

	selectionList = cmds.ls( selection=True, type='transform' )
	startTime = cmds.playbackOptions( query=True, minTime=True )
	endTime = cmds.playbackOptions( query=True, maxTime=True )
	
	for objectName in selectionList:
		cmds.cutKey( objectName, time=(startTime, endTime))

def applyCallback( startTimeField, endTimeField, targetAttributeField, *args ):
	# print 'Apply button pressed.'
	startTime = cmds.intField( startTimeField, query=True, value=True )
	endTime = cmds.intField( endTimeField, query=True, value=True )
	targetAttribute = cmds.textField( targetAttributeField, query=True, text=True )

	selectionList = cmds.ls( selection=True, type='transform' )
	for objectName in selectionList:
		keyFullRotation( objectName, startTime, endTime, targetAttribute)
	

createUI( 'My Title', applyCallback, clearAnimationCallback )
