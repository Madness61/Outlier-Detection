from readFile import read_file, split_dataframe
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import loOuFa1, loOuFa2
from OneClassSVM import oneClassSVM
from Boxplot import boxplot
import pandas as pd

# 82247180 Zeilen in raw1.xyz
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

df3 = []
for k in range(len(splitted)-1):
    outlier = loOuFa1(splitted[k])
    df3.extend(outlier)
print('Number of outlier found with LOF1: ', len(df3))

# df4 = []
# for k in range(len(splitted)-1):
#     outlier = loOuFa2(splitted[k])
#     df4.extend(outlier)
# print('Number of outlier found with LOF2: ', len(df4))

df5 = []
for k in range(len(splitted)-1):
    outlier = oneClassSVM(splitted[k])
    df5.extend(outlier)
print('Number of outlier found with OneClassSVM ', len(df5))
# for k in range(len(splitted)-1):
#     boxplot(splitted[k], 'z')
