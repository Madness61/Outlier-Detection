import pandas as pd
from pyproj import Proj


# Funktion iteriert durch Datei und teilt Daten, die durch ';' getrennt wurden.
def read_file(link):
    lst = []
    with open(link) as file:
        for line in file:

            # Teilt Zeile in Koordinaten auf.
            xyz = [float(x) for x in line.split(";")]
            lst.append(xyz)
    file.close()
    df = pd.DataFrame(data=lst, columns=['lon', 'lat', 'depth'])

    # Transformation des Datensatzes, um die richtigen Koordinaten darzustellen.
    accepted = Proj(proj="utm", zone=26, ellps="WGS84", perserve_units=False)
    df['lon'], df['lat'] = accepted(df['lon'].values, df['lat'].values, inverse=True)
    result = df.loc[:, ['lon', 'lat', 'depth']]
    return result


# Liest alle nicht-Outlier und fügt Spalte hinzu, um dies zu kennzeichnen.
acc = read_file(r"../MSM88_Accepted.txt")
acc['outlier'] = 1
# Liest alle Outlier und fügt Spalte hinzu, um dies zu kennzeichnen.
rej = read_file(r"../MSM88_Rejected.txt")
rej['outlier'] = -1

together = pd.concat([acc, rej])
together.reset_index(drop=True, inplace=True)
together = together.sort_values(by=['lon', 'lat'], ascending=False)
together.reset_index(drop=True, inplace=True)

together['index'] = together.index
together = together[['index', 'lon', 'lat', 'depth', 'outlier']]
together.to_feather('../together_combined.feather')


# Aufteilen der Daten in 1.000.000 Blocks.
fr = pd.DataFrame(data=together)
globalStartIndex = 0
globalEndIndex = 86864832
step = 1000000
startIndex = globalStartIndex
endIndex = startIndex + step

while startIndex <= globalEndIndex:

    df = fr.loc[(fr['index'] >= startIndex) & (fr['index'] <= endIndex-1)]
    df = df.reset_index()
    df.to_feather(f'readFiles/{startIndex}-{endIndex}.feather')
    startIndex += step
    endIndex += step
    if endIndex > globalEndIndex:
        endIndex = globalEndIndex

