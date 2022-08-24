from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd


# Use Spark for large Datasets!
# https://blog.paperspace.com/anomaly-detection-isolation-forest/
def iforest(df):
    pd.options.mode.chained_assignment = None
    z = df['z'].value_counts().index

    model = IsolationForest(contamination='auto', n_estimators=100, max_features=0.4)
    model.fit(df[['z']])

    df['anomaly_score'] = model.decision_function(df[['z']])
    df['iforest'] = model.predict(df[['z']])

    no_anomaly = df.loc[df['iforest'] == 1]
    anomaly = df.loc[df['iforest'] == -1]

    return pd.DataFrame(data=df, columns=['x', 'y', 'z', 'anomaly_score', 'iforest'])

