from partd import pandas
from sklearn.neighbors import LocalOutlierFactor
from sklearn.datasets import make_blobs
from numpy import quantile, where, random
import matplotlib.pyplot as plt
import pandas as pd


def loOuFa1(df):
    new_df = df.copy()
    model = LocalOutlierFactor(n_neighbors=10)
    outlier = model.fit_predict(new_df)
    lof = model.negative_outlier_factor_
    new_df['lof-Score'] = lof
    new_df['lof-Outlier'] = outlier
    # the lowest 3 percent of score values as the anomalies.
    # thresh = quantile(lof, .03)

    return new_df

