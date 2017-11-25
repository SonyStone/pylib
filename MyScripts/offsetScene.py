from pymel.core import *


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


def getTimeConnectedAttributes():
    time = ls(type="time")[0]
    return time.connections(plugs=True)


def reconnectAttributes(outNodeAttribute, inNodeAttributes):
    for connect in inNodeAttributes:
        connectAttr(outNodeAttribute, connect, force = True)


def connectAllTimeToNewTimeCurve():
    if getTimeConnectedAttributes():
        timeCurve = nodetypes.AnimCurveTU(name='timeCurve1')
        setPlaybackTimeKeys(timeCurve)
        reconnectAttributes(timeCurve.output, getTimeConnectedAttributes())


def isPlaybackNotAtStart(startTime):
    return (getPlaybackTime()[0] != startTime)


def getOffset(start, offset):
    return (start - offset)


def offsetPlaybackTime(offset):
    playbackTime = getPlaybackTime()
    playbackOptions( minTime=playbackTime[0] + offset, maxTime=playbackTime[1] + offset )


def setPlaybackToStart(startTime):
    if isPlaybackNotAtStart(startTime):
        offsetPlaybackTime(getOffset(startTime, getPlaybackTime()[0]))


def getAnimCurves():
    allAnimCurves = ls(type='animCurve')
    timeCurves = ls(regex='_{2}(anim)\w+')
    return [x for x in allAnimCurves if x not in timeCurves]


def setKeysToStart(start):
    for animCurve in getAnimCurves():  
        keyframe(animCurve, edit=True, relative=True, timeChange=getOffset(start, getPlaybackTime()[0]))


connectAllTimeToNewTimeCurve()
setKeysToStart(1)
setPlaybackToStart(1)
