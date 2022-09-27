import numpy as np
import pandas as pd


# Implementierung der IQR.
def IQR_Method(df):
    # Berechnung des ersten und dritten Quartils.
    q3, q1 = np.percentile(df['depth'], [75, 25])
    iqr = q3 - q1

    # Datenpunkte über der oberen Schranke.
    upper = df[df['depth'] >= (q3 + 1.5 * iqr)]
    # Datenpunkte unter der unteren Schranke.
    lower = df[df['depth'] <= (q1 - 1.5 * iqr)]

    # Nimmt sich alle Datenpunkte, die sich außerhalb der Schranken befindet.
    anomaly = pd.concat([lower, upper])
    df_diff = pd.concat([df, anomaly]).drop_duplicates(keep=False)

    anomaly['iqr-Outlier'] = -1
    df_diff['iqr-Outlier'] = 1

    together = pd.concat([anomaly, df_diff])
    return together

