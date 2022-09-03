from partd import pandas
from sklearn.neighbors import LocalOutlierFactor
from sklearn.datasets import make_blobs
from numpy import quantile, where, random
import matplotlib.pyplot as plt
import pandas as pd


def lof(old_df):
    df = old_df.copy()

    model = LocalOutlierFactor(n_neighbors=5, metric="manhattan",novelty=True)
    model.fit(df.values)
    outlier = model.predict(df)
    score = model.negative_outlier_factor_
    df['lof-Score'] = -score
    df['lof-Outlier'] = outlier

    # the lowest 3 percent of score values as the anomalies.
    # thresh = quantile(lof, .03)
    return df

