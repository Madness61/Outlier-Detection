from sklearn.svm import OneClassSVM
import pandas as pd


def oneClassSVM(df):
    svm = OneClassSVM(nu=0.1, gamma='auto')
    svm.fit(df)
    pred = svm.predict(df)
    #model = clf.predict(df)
    #print(pred)
    #anomaly = df.loc[model == -1]
    #print(anomaly.columns)
    #df_diff = pd.concat([df, anomaly]).drop_duplicates(keep=False)
    #anomaly['svm'] = -1
    #df_diff['svm'] = 1
    #together = pd.concat([anomaly, df_diff])
    #together = together.sort_values(by=['x'])
    #return together
