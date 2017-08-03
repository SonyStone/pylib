from pymel.core import *

def getAnimCurves():
    allAnimCurves = ls(type='animCurve')
    timeCurves = ls(regex='_{2}(anim)\w+')
    return [x for x in allAnimCurves if x not in timeCurves]

def getAnimCurvesAttributes():
    allAnimCurves = ls(type='animCurve')
    timeCurves = ls(regex='_{2}(anim)\w+')
    return [x.input for x in allAnimCurves if x not in timeCurves]

def getPlaybackTime():
    return [
        playbackOptions(query=True, minTime=True),
        playbackOptions(query=True, maxTime=True)
    ]

def setPlaybackTimeKeys(animCurve):
    playbackTime = getPlaybackTime()
    first = 0
    while animCurve.numKeys() > first:
        animCurve.remove(first)

    for index in range(len(playbackTime)):
        animCurve.addKey(playbackTime[index], playbackTime[index], tangentInType='smooth', tangentOutType='smooth' )

    animCurve.setPreInfinityType('linear', change=None)
    animCurve.setPostInfinityType('linear', change=None)
    return animCurve

def setAnimTimeCurve():
    animCurve = nodetypes.AnimCurveTU(name='__animTimeCurve1')
    setPlaybackTimeKeys(animCurve)
    return animCurve

def reconnectAttributes(outNodeAttribute, inNodeAttributes):
    for connect in inNodeAttributes:
        connectAttr(outNodeAttribute, connect, force = True)

def allCurvesConnectToTimeCurve():
    animTimeCurve = setAnimTimeCurve()
    reconnectAttributes(animTimeCurve.output, getTimeConnectedAttributes())
    reconnectAttributes(animTimeCurve.output, getAnimCurvesAttributes())

allCurvesConnectToTimeCurve()