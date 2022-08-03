import numpy as np


def IQR_Method(df):
    print("Old Shape: ", df.shape)

    q3, q1 = np.percentile(df['z'], [75, 25])
    iqr = q3 - q1

    # Upper bound
    upper = np.where(df['z'] >= (q3 + 1.5 * iqr))
    # print('upper: ')
    # print(upper[0])

    # Lower bound
    lower = np.where(df['z'] <= (q1 - 1.5 * iqr))
    # print('lower: ')
    # print(lower[0])

    df.drop(upper[0], inplace=True)
    df.drop(lower[0], inplace=True)

    print("New Shape: ", df.shape)

