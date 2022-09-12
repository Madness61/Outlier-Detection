import pandas as pd
from pyproj import Proj



def read_file():
    lst = []
    # Gets all coordinates from file and writes it in lst as Martix.
    with open(r"C:/Users/manue/OneDrive/Desktop/BA/raw1.xyz") as file:
        count = 0
        for line in file:
            # Can delete, to look at full dataset.
            if count >= 200000:
                break

            # Splits every coordinate in each line and cast float.
            xyz = [float(x) for x in line.split("\t")]
            lst.append(xyz)
            count = count + 1
    file.close()
    return pd.DataFrame(data=lst, columns=['lon', 'lat', 'depth'])


def read_accepted(link, limit):
    lst = []
    with open(link) as file:
        count = 0
        for line in file:
            # Can delete, to look at full dataset.
            if count >= limit:
                break
            print(count)
            # Splits every coordinate in each line and cast float.
            xyz = [float(x) for x in line.split(";")]
            lst.append(xyz)
            count = count + 1
    file.close()
    df = pd.DataFrame(data=lst, columns=['lon', 'lat', 'depth'])
    accepted = Proj(proj="utm", zone=26, ellps="WGS84", perserve_units=False)
    df['lon'], df['lat'] = accepted(df['lon'].values, df['lat'].values, inverse=True)
    result = df.loc[:, ['lon', 'lat', 'depth']]
    return result


def getFile():
    raw = read_file()
    raw = raw.sort_values(by=['lon'])
    raw.reset_index(inplace=True)
    #raw.to_feather('raw.feather')

    acc = read_accepted(r"../MSM88_Accepted.txt", 830000)
    acc['outlier'] = 1
    rej = read_accepted(r"../MSM88_Rejected.txt", 170000)
    rej['outlier'] = -1

    together = pd.concat([acc, rej])
    together.reset_index(drop=True, inplace=True)
    together = together.sort_values(by=['lon'], ascending=False)
    together.reset_index(drop=True, inplace=True)

    together['index'] = together.index
    together = together[['index', 'lon', 'lat', 'depth', 'outlier']]
    print('Data read')
    return together
