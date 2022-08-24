from partd import pandas
from sklearn.neighbors import LocalOutlierFactor
from sklearn.datasets import make_blobs
from numpy import quantile, where, random
import matplotlib.pyplot as plt
import pandas as pd


def loOuFa1(df):
    pd.options.mode.chained_assignment = None
    model1 = LocalOutlierFactor(n_neighbors=10)
    y_pred = model1.fit_predict(df)

    #outlier_index = where(y_pred == -1)
    #outlier_values = df.iloc[outlier_index]

    df['lof'] = y_pred
    return df

