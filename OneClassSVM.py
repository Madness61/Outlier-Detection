from sklearn.svm import OneClassSVM


def oneClassSVM(df_old):
    df = df_old.copy()

    outlier = len(df[df['outlier'] == -1]) / len(df)
    if outlier >= 0.5:
        outlier = 0.5
    if outlier <= 0:
        outlier = 0

    svm = OneClassSVM(kernel='rbf', gamma=0.001, nu=outlier).fit(df[['lon', 'lat', 'depth']].values)
    pred = svm.predict(df[['lon', 'lat', 'depth']].values)
    scores = svm.decision_function(df[['lon', 'lat', 'depth']].values)

    df['svm-Score'] = scores
    df['svm-Outlier'] = pred
    return df
