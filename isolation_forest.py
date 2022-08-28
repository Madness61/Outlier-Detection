from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd


# Use Spark for large Datasets!
# https://blog.paperspace.com/anomaly-detection-isolation-forest/
def iforest(df):
    new_df = df.copy()
    z = new_df['z'].value_counts().index

    model = IsolationForest(contamination='auto', n_estimators=100, max_features=0.4)
    model.fit(new_df[['z']])

    new_df['ifor-Score'] = model.decision_function(new_df[['z']])
    new_df['ifor-Outlier'] = model.predict(new_df[['z']])

    # no_anomaly = df.loc[df['iforest'] == 1]
    # anomaly = df.loc[df['iforest'] == -1]

    return new_df

