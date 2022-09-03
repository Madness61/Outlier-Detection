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



def backup(df):
    new_df = df.copy()
    z = new_df[['z']].values
    model = IsolationForest()
    model.fit(new_df)
    pred = model.predict(new_df)
    new_df['ifor-Score'] = model.decision_function(new_df)
    new_df['ifor-Outlier'] = pred
    import plotly.express as px
    anomalies = new_df[new_df['ifor-Outlier'] == -1]
    # importing the plot
    import plotly.graph_objects as go
    # importing the module
    import seaborn as sns

    # setting the size of plotting
    sns.set(rc={'figure.figsize': (8, 4)})

    # plotting bar plot
    sns.countplot(new_df['ifor-Outlier'])
    plt.show()
    return new_df

    #X_explain = X_test
    #shap_values = shap.TreeExplainer(clf).shap_values(X_explain)
    #shap.summary_plot(shap_values, X_explain)
