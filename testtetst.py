import numpy as np
import pandas as pd
from readFile import split_dataframe, read_file


df = read_file()
splitted = split_dataframe(df, chunk_size=100)

q3, q1 = np.percentile(df['z'], [75, 25])
iqr = q3 - q1

    # Upper bound
upper = df[df['z'] >= (q3 + 1.5 * iqr)]

    # Lower bound
lower = df[df['z'] <= (q1 - 1.5 * iqr)]


frames = pd.concat([lower, upper])

