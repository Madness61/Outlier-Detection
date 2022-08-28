import numpy as np
import pandas as pd


def IQR_Method(df):

    q3, q1 = np.percentile(df['z'], [75, 25])
    iqr = q3 - q1

    # Upper bound
    upper = df[df['z'] >= (q3 + 1.5 * iqr)]
    # Lower bound
    lower = df[df['z'] <= (q1 - 1.5 * iqr)]

    anomaly = pd.concat([lower, upper])
    df_diff = pd.concat([df, anomaly]).drop_duplicates(keep=False)

    anomaly['iqr-Outlier'] = -1
    df_diff['iqr-Outlier'] = 1

    together = pd.concat([anomaly, df_diff])
    together = together.sort_values(by=['x'])
    return together

