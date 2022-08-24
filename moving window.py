import math
import time
import sys
import pandas as pd
import numpy as np

if len(sys.argv) > 1:
    ################config moving window######
    global upperBorderMultiplicator
    upperBorderMultiplicator = 1.2
    windowRadius = float(sys.argv[3])
    windowName = f'{windowRadius}km'
    windowBoundaries = 0.01 * windowRadius
    np.set_printoptions(threshold=sys.maxsize)
    secondRadius = float(sys.argv[4])
    secondWindow = f'{secondRadius}km'

    globalStartIndex = float(sys.argv[1]).__round__(0)
    globalEndIndex = float(sys.argv[2]).__round__(0)
    step = 100000
    startIndex = globalStartIndex
    endIndex = startIndex + step
else:
    upperBorderMultiplicator = 1.2
    windowRadius = 1
    windowName = f'{windowRadius}km'
    windowBoundaries = 0.01 * windowRadius
    np.set_printoptions(threshold=sys.maxsize)
    secondRadius = 0.2
    secondWindow = f'{secondRadius}km'

    globalStartIndex = 0
    globalEndIndex = 10000
    step = 5000
    startIndex = globalStartIndex
    endIndex = startIndex + step


#Hier noch eine Quelle einfügen. Haversine Vectorized...
def calculateWindow(lon1, lat1, dataFrame, radius):
    return dataFrame[6371 * 2 * np.arcsin(np.sqrt(
        np.sin((np.radians(dataFrame['lat']) - math.radians(lat1)) / 2) ** 2 + math.cos(
            math.radians(lat1)) * np.cos(np.radians(dataFrame['lat'])) * np.sin(
            (np.radians(dataFrame['lon']) - math.radians(lon1)) / 2) ** 2)) < radius]


def calculateFeatures(entry, windowName, windowBoundaries, windowRadius, endIndex, startIndex, secondRadius,
                      secondWindow):
    # get moving window for entry
    global filterFrame
    global upperBorderMultiplicator
    if (entry['index'] <= endIndex and entry['index'] >= startIndex):
        if filterFrame['lon'].max() < entry['lon'] + windowBoundaries:
            filterFrame = dataFrame.loc[(entry['lon'] - windowBoundaries < dataFrame['lon']) & (
                    entry['lon'] + upperBorderMultiplicator * windowBoundaries > dataFrame['lon'])]
            print(f"      new window for index {entry['index']} in {((time.time() - start_time) / 60)} minutes ---")

        #        calculateFeaturesForWindow(entry, filterFrame, windowBoundaries, windowName, windowRadius)
        calculateFeaturesForWindow(entry, filterFrame, windowBoundaries, '0.1km', 0.1)


def calculateFeaturesForWindow(entry, filterFrame, windowBoundaries, windowName, windowRadius):
    print(f"calculate for entry {entry['index']}")
    window = calculateWindow(entry['lon'], entry['lat'], filterFrame.loc[
        ((filterFrame['lon'] > entry['lon'] - windowBoundaries) & (
                filterFrame['lon'] < entry['lon'] + windowRadius * 0.01))], windowRadius)
    dataFrame.loc[entry.name, f'std{windowName}'] = window[
        'depth'].std()
    # durchschnittliche Tiefe im Fenster
    dataFrame.loc[entry.name, f'meanWindowDepth{windowName}'] = window[
        'depth'].mean()
    # Differenz Tiefe zur durschnittlichen Tiefe im Fenster (sollte kleiner als die Std sein)
    dataFrame.loc[entry.name, f'dif{windowName}'] = \
        window[window['index'] == entry['index']]['depth'].mean() - dataFrame.loc[
            entry.name, f'meanWindowDepth{windowName}']
    dataFrame.loc[entry.name, f'dataInRadius{windowName}'] = window['index'].count()
    dataFrame.loc[entry.name, f'medianWindowDepth{windowName}'] = window['depth'].median()
    dataFrame.loc[entry.name, f'diffDepthToStdError{windowName}'] = abs(
        abs(dataFrame.loc[entry.name, f'dif{windowName}']) - abs(dataFrame.loc[entry.name, f'std{windowName}']))
    dataFrame[f'normalisedDistanceToStd{windowRadius}km'] = abs(dataFrame[f'dif{windowRadius}km']) / abs(
        dataFrame[f'std{windowRadius}km'])
    dataFrame[f'difFromDepthToMedian{windowRadius}km'] = abs(
        abs(entry['depth']) - abs(dataFrame.loc[entry['index']][f'medianWindowDepth{windowName}']))


def getBoundariesForIndex(lowerIndex, upperIndex, windowName):
    newlyReadDf = pd.read_feather('feather_combined')
    newlyReadDf[windowName] = 0
    newlyReadDf[windowName] = newlyReadDf[windowName].astype('object')
    newlyReadDf = newlyReadDf.loc[
        (newlyReadDf[newlyReadDf['index'] == lowerIndex]['lon'].max() - windowBoundaries < newlyReadDf['lon']) & (
                newlyReadDf[newlyReadDf['index'] == upperIndex][
                    'lon'].max() + upperBorderMultiplicator * windowBoundaries >
                newlyReadDf['lon'])]
    print(f'dataFrame for {lowerIndex} until {upperIndex} created')
    return newlyReadDf


while startIndex <= globalEndIndex:
    start_time = time.time()
    dataFrame = getBoundariesForIndex(startIndex, endIndex, windowName)
    global filterFrame
    filterFrame = dataFrame[0:1]
    dataFrame[windowName] = 0
    dataFrame[windowName] = dataFrame[windowName].astype('object')
    dataFrame.apply(calculateFeatures,
                    args=(windowName, windowBoundaries, windowRadius, endIndex, startIndex, secondRadius, secondWindow),
                    axis=1)
    dataFrame = dataFrame.loc[(dataFrame['index'] >= startIndex) & (dataFrame['index'] <= endIndex)]
    print(f'calculations for {startIndex} to {endIndex} finished')
    dataFrame = dataFrame.reset_index()
    dataFrame.to_feather(f'result/{startIndex}-{endIndex}.feather')
    print(f'index from {startIndex} to index{endIndex} calculated and saved')
    print("--- %s minutes ---" % ((time.time() - start_time) / 60))
    startIndex += step
    endIndex += step
    if endIndex > globalEndIndex:
        endIndex = globalEndIndex

# https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01
print("start exporting")
print(f'finished {globalStartIndex}')
print("--- %s minutes ---" % ((time.time() - start_time) / 60))