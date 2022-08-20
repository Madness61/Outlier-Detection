from numpy import quantile
from sklearn.neighbors import LocalOutlierFactor


def loOuFa1(df):

    lof = LocalOutlierFactor()
    model = lof.fit_predict(df)
    anomaly = df.loc[model == -1]

    return anomaly


def loOuFa2(df):

    model = LocalOutlierFactor(n_neighbors=60)
    model.fit_predict(df)
    lof = model.negative_outlier_factor_
    thresh = quantile(lof, .04)
    anomaly = df.loc[lof <= thresh]

    index = anomaly.index.tolist()
    return anomaly
