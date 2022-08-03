from sklearn.ensemble import IsolationForest
import numpy as np
from main import df


# Use Spark for large Datasets!
# https://blog.paperspace.com/anomaly-detection-isolation-forest/

z = df['z'].value_counts().index

model = IsolationForest(contamination='auto', n_estimators=100, max_features=0.4)
model.fit(df[['z']])

df['anomaly_scores'] = model.decision_function(df[['z']])
df['anomaly'] = model.predict(df[['z']])
no_anomaly = df.loc[df['anomaly'] == 1]
anomaly = df.loc[df['anomaly'] == -1]

print('No Anomaly:', len(no_anomaly))
print('Anomaly: ', len(anomaly))


