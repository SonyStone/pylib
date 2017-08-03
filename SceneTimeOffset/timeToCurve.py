from pymel.core import *

def timeToCurve():
    
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
            obj.addKey(playbackTime[index], playbackTime[index], tangentInType='spline', setOutTangentType='spline' )

        obj.setPreInfinityType('linear', change=None)
        obj.setPostInfinityType('linear', change=None)
        return obj

    time = ls(type="time")[0]
    timeConnectedAttributes = time.connections(plugs=True)

    animTimeCurve = nodetypes.AnimCurveTU(name='animTimeCurve1')
    playbackToKeys(animTimeCurve)

    for connect in timeConnectedAttributes:
        connectAttr(animTimeCurve.output, connect, force = True)


timeToCurve()