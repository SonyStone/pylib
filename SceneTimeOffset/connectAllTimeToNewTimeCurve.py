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

connectAllTimeToNewTimeCurve()

# todo:
    # reconnect all node attribut out connection to the new one node
    # make time class for time.getPlayback, time.getConnectedAttributes, and other