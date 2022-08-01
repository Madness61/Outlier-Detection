from Boxplot import boxplot
from readFile import df
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
import numpy as np

# Isolation Forest

X = df[['x', 'y', 'z']]
y = []

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = IsolationForest(random_state=0)
clf.fit(X_train)
y_pred = clf.predict(X_test)

pred = pd.DataFrame({'pred': y_pred})
pred['y_pred'] = np.where(pred['pred'] == -1, 1, 0)
y_pred = pred['y_pred']
print("Precision:", precision_score(y_test, y_pred))

