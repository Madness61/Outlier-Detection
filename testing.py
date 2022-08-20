from matplotlib import pyplot as plt
from main import df, df1, df2, df3, df5
import pandas as pd
from functools import reduce

df12 = df1.merge(df2, how='inner')
df123 = df12.merge(df3, how='inner')
anomaly = df123.merge(df5, how='inner')

print('Number of outlier that all have together: ', len(anomaly))

temp = pd.merge(df, anomaly, how="outer", indicator=True).query('_merge=="left_only"')
cleaned = temp.drop(columns=['anomaly_scores', 'anomaly', '_merge'])


# 3D-View of coordinates.
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.scatter3D(cleaned['x'], cleaned['y'], cleaned['z'], c='blue')
ax.scatter3D(anomaly['x'], anomaly['y'], anomaly['z'], c='red')
#ax.scatter3D(df1['x'], df1['y'], df1['z'], c='green')
#ax.scatter3D(df2['x'], df2['y'], df2['z'], c='orange')
#ax.scatter3D(df3['x'], df3['y'], df3['z'], c='yellow')
#ax.scatter3D(df5['x'], df5['y'], df5['z'], c='pink')
plt.show()
