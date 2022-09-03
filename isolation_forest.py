import matplotlib.pyplot as plt
from pygments.lexers import go
from sklearn.ensemble import IsolationForest
import numpy as np
import pandas as pd
import shap
# importing the module
from sklearn.metrics import accuracy_score
# Use Spark for large Datasets!
# https://blog.paperspace.com/anomaly-detection-isolation-forest/
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split


def iforest(old_df):
    df = old_df.copy()

    X = df[['x', 'y', 'z']]
    y = df['outlier']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
    clf = IsolationForest(max_samples=len(X_train))
    clf.fit(X_train)
    # making predictions
    y_pred = clf.predict(X_test)
    # finding the accuracy
    print(accuracy_score(y_pred, y_test))
    score_train = clf.score_samples(X_train)
    score_test = clf.score_samples(X_test)
    df['ifor-Score'] = pd.concat([score_train, score_test])



    #df['ifor-Outlier'] = model.predict(z)



    return df



def backup(old_df):
    df = old_df.copy()
    outlier = len(df[df['outlier'] == -1]) / 1000
    if outlier >= 0.5:
        outlier = 0.5

    model = IsolationForest(random_state=0, contamination=outlier)
    model.fit(df)
    pred = model.predict(df)
    scores = model.decision_function(df)
    df['ifor-Outlier'] = pred
    df['ifor-Score'] = scores
    return df

    #X_explain = X_test
    #shap_values = shap.TreeExplainer(clf).shap_values(X_explain)
    #shap.summary_plot(shap_values, X_explain)
