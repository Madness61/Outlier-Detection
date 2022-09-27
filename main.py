import pandas as pd
from eveltlogGenerater import getEventlog
from feature_calculation import calcFeature


# Holt sich einen 1.000.000 großen Block, welcher in readFile.py erzeugt wurde.
comb_df = pd.read_feather('readFiles/52000000-53000000.feather')

# Anwenden der Methoden und speichern der Ergebnisse.
all_df = calcFeature(comb_df)
all_df.to_csv('../result/52000000-53000000.csv')

# Erstellung der Eventlogs und speichern der Ergebnisse.
eventlog = getEventlog(comb_df, all_df)
eventlog.to_csv('../eventlogs/52000000-53000000.csv')

