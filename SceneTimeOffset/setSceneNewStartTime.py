from pymel.core import *
# from connectAllTimeToNewTimeCurve import *

def getPlaybackTime():
    return [
        playbackOptions(query=True, minTime=True),
        playbackOptions(query=True, maxTime=True)
    ]

def isPlaybackNotAtStart(startTime):
    return (getPlaybackTime()[0] != startTime)

def getOffset(start, offset):
    return (start - offset)

def offsetPlaybackTime(offset):
    playbackTime = getPlaybackTime()
    playbackOptions( minTime=playbackTime[0] + offset, maxTime=playbackTime[1] + offset )

def setToStart(startTime):
    if isPlaybackNotAtStart(startTime):
        offsetPlaybackTime(getOffset(startTime, getPlaybackTime()[0]))

setToStart(1)