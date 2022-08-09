from readFile import read_file, split_dataframe
from IQR_Method import IQR_Method
from isolation_forest import iforest
from Boxplot import boxplot
import pandas as pd

df = read_file()
splitted = split_dataframe(df, chunk_size=1000)

df1 = []
for k in range(len(splitted)-1):
    outlier = IQR_Method(splitted[k])
    df1.extend(outlier)
print('Number of outlier found with IQR: ', len(df1))


df2 = []
for k in range(len(splitted)-1):
    outlier = iforest(splitted[k])
    df2.extend(outlier)
print('Number of outlier found with IForest: ', len(df2))


# for k in range(len(splitted)-1):
#     boxplot(splitted[k], 'z')
