from sklearn.ensemble import IsolationForest


# Implementierung des Isolation Forests.
def iforest(old_df):
    df = old_df.copy()
    # Parameter für contamination Score. Berechnet den Anteil an Outliern in dem Chunk.
    # Falls dieser über 50% ist muss er auf 0.5 gecappt werden.
    outlier = len(df[df['outlier'] == -1]) / len(df)
    if outlier >= 0.5:
        outlier = 0.5
    if outlier <= 0:
        outlier = 0

    # contamination-Score gibt Prozentanteil an Outliern an.
    model = IsolationForest(contamination=outlier)
    model.fit(df[['lon', 'lat', 'depth']].values)
    pred = model.predict(df[['lon', 'lat', 'depth']].values)
    scores_raw = model.decision_function(df[['lon', 'lat', 'depth']].values)
    # Transformiert die Score-Werte, damit diese anschaulicher sind (für die spätere Klassifizierung).
    scores = [-1 * s + 0.5 for s in scores_raw]
    df['ifor-Outlier'] = pred
    df['ifor-Score'] = scores
    return df
