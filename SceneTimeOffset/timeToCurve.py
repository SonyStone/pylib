from pymel.core import *

def timeToCurve():
    
    def playbackToKeys(obj):
        first = 0
        last = 1
        startTime = playbackOptions(query=True, minTime=True)
        endTime = playbackOptions(query=True, maxTime=True)
        

        while obj.numKeys() > 0:
            obj.remove(first)
        
        obj.addKey(endTime, endTime, tangentInType='linear')
        obj.addKey(startTime, startTime, tangentInType='linear')
    
        return obj

    timeConnectedAttributes = time.connections(plugs=True)

    animTimeCurve = nodetypes.AnimCurveTU(name='animTimeCurve1')
    playbackToKeys(animTimeCurve)

    for connect in timeConnectedAttributes:
        connectAttr(animTimeCurve.output, connect, force = True)


timeToCurve()