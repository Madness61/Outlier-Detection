import pandas as pd
from matplotlib import pyplot as plt

from readFile import read_file, split_dataframe, read_accepted
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import loOuFa1, loOuFa2
from OneClassSVM import oneClassSVM
from Boxplot import boxplot

# 82247180 Zeilen in raw1.xyz
df = read_file()
splitted = split_dataframe(df, chunk_size=1000)

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()

#for k in range(len(splitted)-1):
#    iqr = IQR_Method(splitted[k])
#    df1 = pd.concat([df1, iqr])

#    ifor = iforest(splitted[k])
#    df2 = pd.concat([df2, ifor])

#    lof = loOuFa1(splitted[k])
#    df3 = pd.concat([df3, lof])

#    svm = oneClassSVM(splitted[k])
#    df5 = pd.concat([df5, svm])

#print('Number of outlier found with IQR: ', len(df1))
#anomaly = df2.loc[df2['anomaly'] == -1]
#print('Number of outlier found with IForest: ', len(anomaly))
#print('Number of outlier found with LOF1: ', len(df3))
#print(df3)
#print('Number of outlier found with OneClassSVM ', len(df5))

#print(df2.loc[df2['anomaly_score'] < -0.1])
#print(df3.loc[df['anomaly_scores'] < -0.7])
#print(df5.loc[df['anomaly_scores'] < -0.7])


# df4 = pd.DataFrame()
# for k in range(len(splitted)-1):
#     outlier = loOuFa2(splitted[k])
#     df4 = pd.concat([df4, outlier])
# print('Number of outlier found with LOF2: ', len(df4))

# for k in range(len(splitted)-1):
boxplot(splitted[0], 'z')

