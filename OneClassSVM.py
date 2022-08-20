from sklearn.svm import OneClassSVM


def oneClassSVM(df):
    clf = OneClassSVM(nu=0.1, gamma='auto').fit(df)
    model = clf.predict(df)
    anomaly = df.loc[model == -1]
    index = anomaly.index.tolist()
    return anomaly
