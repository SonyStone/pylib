from pymel.core import *

def playbackToKeys(obj):
    first = 0
    last = 1
    playbackTime = [
        playbackOptions(query=True, minTime=True),
        playbackOptions(query=True, maxTime=True)
    ]
    
    while obj.numKeys() > first:
        obj.remove(first)

    for index in range(2):
        obj.addKey(playbackTime[index], playbackTime[index], tangentInType='linear')
        obj.setInTangentType(index, 'linear', change=None)
        obj.setOutTangentType(index, 'linear', change=None)

    obj.setPreInfinityType('linear', change=None)
    obj.setPostInfinityType('linear', change=None)
    return obj

animTimeCurve = nodetypes.AnimCurveTU(name='animTimeCurve1')
playbackToKeys(animTimeCurve)

