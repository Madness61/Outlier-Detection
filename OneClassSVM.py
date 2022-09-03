import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM, SVC
import pandas as pd


def oneClassSVM(df_old):
    df = df_old.copy()
    svm = OneClassSVM(kernel="rbf", gamma='auto')
    svm.fit(df)
    pred = svm.predict(df)
    scores = svm.score_samples(df)

    df['ocsvm-Score'] = scores
    df['ocsvm-Outlier'] = pred
    return df
