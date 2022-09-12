from sklearn.ensemble import IsolationForest


def iforest(old_df):
    df = old_df.copy()
    outlier = len(df[df['outlier'] == -1]) / len(df)
    if outlier >= 0.5:
        outlier = 0.5
    if outlier <= 0:
        outlier = 0

    model = IsolationForest(contamination=outlier)
    model.fit(df[['lon', 'lat', 'depth']].values)
    pred = model.predict(df[['lon', 'lat', 'depth']].values)
    scores_raw = model.decision_function(df[['lon', 'lat', 'depth']].values)
    scores = [-1 * s + 0.5 for s in scores_raw]
    df['ifor-Outlier'] = pred
    df['ifor-Score'] = scores
    return df
