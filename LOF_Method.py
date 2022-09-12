from sklearn.neighbors import LocalOutlierFactor


def lof(old_df):
    df = old_df.copy()

    outlier = len(df[df['outlier'] == -1]) / len(df)
    if outlier >= 0.5:
        outlier = 0.5
    if outlier <= 0:
        outlier = 0
    model = LocalOutlierFactor(contamination=outlier, n_neighbors=50, p=2)
    outlier = model.fit_predict(df[['lon', 'lat', 'depth']].values)
    score = model.negative_outlier_factor_
    df['lof-Score'] = -score
    df['lof-Outlier'] = outlier
    return df
