import datetime as dt

import pandas as pd

from eveltlogGenerater import getEventlog
from feature_calculation import calcFeature
from readFile import getFile

start = dt.datetime.now()

#comb_df = getFile()
#comb_df.to_feather('together_combined.feather')
comb_df = pd.read_feather('together_combined.feather')
#comb_df.to_csv('../bla.csv')

all_df = calcFeature(comb_df)
print(all_df.columns)
all_df.to_csv('../all.csv')

eventlog = getEventlog(comb_df, all_df)
eventlog.to_csv('../eventlog.csv')
end = dt.datetime.now()
print('time it took: ', end - start)
