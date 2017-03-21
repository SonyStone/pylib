# clearAnimation.py
import maya.cmds as cmds

selectionList = cmds.ls( selection=True, type='transform' )
startTime = cmds.playbackOptions( query=True, minTime=True )
endTime = cmds.playbackOptions( query=True, maxTime=True )

for objectName in selectionList:
    cmds.cutKey( objectName, time=(startTime, endTime))