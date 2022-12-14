import time
import sys
import pandas as pd
import numpy as np


# Versuch des Moving-Window-Ansatzes. Wurde schlussendlich verworfen, da die Bedingung der Boundaries
# aus unerfindlichen Gründen nur leere Dataframes erzeugten.

upperBorderMultiplicator = 1.2
windowRadius = 1
windowName = f'{windowRadius}km'
windowBoundaries = 0.01 * windowRadius
np.set_printoptions(threshold=sys.maxsize)
secondRadius = 0.2
secondWindow = f'{secondRadius}km'

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

    print('Lowerindex: ', lowerIndex)
    print('col: \n', newlyReadDf['index'])
    print(newlyReadDf[newlyReadDf['index'] == lowerIndex])
    print(f'dataFrame for {lowerIndex} until {upperIndex} created')
    return newlyReadDf


while startIndex <= globalEndIndex:
    start_time = time.time()
    dataFrame = getBoundariesForIndex(startIndex, endIndex)
    print('start :', startIndex)
    print('end :', endIndex)
    print('name :', windowName)

    global filterFrame
    filterFrame = dataFrame[0:1]

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

# https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01
print("start exporting")
print(f'finished {globalStartIndex}')
print("--- %s minutes ---" % ((time.time() - start_time) / 60))