import pandas as pd
import numpy as np
from pyproj import Proj
import pyarrow


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
    return pd.DataFrame(data=lst, columns=['x', 'y', 'z'])


def read_accepted(link):
    lst = []
    with open(link) as file:
        count = 0
        for line in file:
            # Can delete, to look at full dataset.
            if count >= 100000:
                break

            # Splits every coordinate in each line and cast float.
            xyz = [float(x) for x in line.split(";")]
            lst.append(xyz)
            count = count + 1
    file.close()
    df = pd.DataFrame(data=lst, columns=['x', 'y', 'z'])
    accepted = Proj(proj="utm", zone=26, ellps="WGS84", perserve_units=False)
    df['x'], df['y'] = accepted(df['x'].values, df['y'].values, inverse=True)
    result = df.loc[:, ['x', 'y', 'z']]
    return result


raw = read_file()
raw = raw.sort_values(by=['x'])
raw.reset_index(inplace=True)
raw.to_feather('raw.feather')

acc = read_accepted(r"C:/Users/manue/OneDrive/Desktop/MSM88_Accepted.txt")
acc['outlier'] = 1
rej = read_accepted(r"C:/Users/manue/OneDrive/Desktop/MSM88_Rejected.txt")
rej['outlier'] = -1

together = pd.concat([acc, rej])
together = together.sort_values(by=['x'])
together.reset_index(inplace=True)
together.to_feather('together_combined.feather')
print('done')
