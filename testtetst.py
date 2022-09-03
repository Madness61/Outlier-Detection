import math
import time
import sys
import pandas as pd
import numpy as np


windowRadius = 1
windowName = f'{windowRadius}km'
windowBoundaries = 0.01 * windowRadius
np.set_printoptions(threshold=sys.maxsize)
upperBorderMultiplicator = 1.2

globalStartIndex = 0
globalEndIndex = 20000
step = 5000
startIndex = globalStartIndex
endIndex = startIndex + step


def getBoundariesForIndex(lowerIndex, upperIndex):
    newlyReadDf = pd.read_feather('together_combined.feather')
    newlyReadDf = newlyReadDf.loc[
        (newlyReadDf[newlyReadDf['index'] == lowerIndex]['x'].max() - windowBoundaries < newlyReadDf['x']) & (
                newlyReadDf[newlyReadDf['index'] == upperIndex][
                    'x'].max() + upperBorderMultiplicator * windowBoundaries >
                newlyReadDf['x'])]
    print(newlyReadDf)
    return newlyReadDf


while startIndex < globalEndIndex:
    start_time = time.time()
    dataFrame = getBoundariesForIndex(startIndex, endIndex)
    global filterFrame
    filterFrame = dataFrame[0:1]
    dataFrame[windowName] = 0
    dataFrame[windowName] = dataFrame[windowName].astype('object')

    dataFrame = dataFrame.loc[(dataFrame['index'] >= startIndex) & (dataFrame['index'] <= endIndex)]
    print(f'calculations for {startIndex} to {endIndex} finished')
    dataFrame = dataFrame.reset_index()
    dataFrame.to_feather(f'result/{startIndex}-{endIndex}.feather')
    print(f'index from {startIndex} to index {endIndex} calculated and saved')
    print("--- %s minutes ---" % ((time.time() - start_time) / 60))
    startIndex += step
    endIndex += step
    if endIndex >= globalEndIndex:
        endIndex = globalEndIndex

