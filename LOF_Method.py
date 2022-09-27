from sklearn.neighbors import LocalOutlierFactor


# Implementierung des Local Outlier Factors.
def lof(old_df):
    df = old_df.copy()
    # Siehe Bweschreibung Isolation Forest
    outlier = len(df[df['outlier'] == -1]) / len(df)
    if outlier >= 0.5:
        outlier = 0.5
    if outlier <= 0:
        outlier = 0
    # Da Methode auf 1.000.000-Blöcke angewendet wird, wurde die Anzahl der Nachbarn auf 50 erhöht.
    model = LocalOutlierFactor(contamination=outlier, n_neighbors=50, p=2)
    outlier = model.fit_predict(df[['lon', 'lat', 'depth']].values)
    score = model.negative_outlier_factor_
    df['lof-Score'] = -score
    df['lof-Outlier'] = outlier
    return df
