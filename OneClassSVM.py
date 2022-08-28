from sklearn.svm import OneClassSVM
import pandas as pd


def oneClassSVM(df):
    new_df = df.copy()
    svm = OneClassSVM(nu=0.1, gamma='auto')
    svm.fit(new_df)
    pred = svm.predict(new_df)
    scores = svm.score_samples(new_df)

    new_df['ocsvm-Score'] = scores
    new_df['ocsvm-Outlier'] = pred

    return new_df
