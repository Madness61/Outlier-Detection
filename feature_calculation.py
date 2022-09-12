import pandas as pd
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import lof
from OneClassSVM import oneClassSVM
import numpy as np
from sklearn.metrics import accuracy_score


def split_dataframe(df, chunk_size):
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks


def calcFeature(comb_df):
    # 82247180 Zeilen in raw1.xyz
    #raw_df = pd.read_feather('raw.feather')

    splitted = split_dataframe(comb_df, 1000)
    iqr_df = pd.DataFrame()
    ifor_df = pd.DataFrame()
    svm_df = pd.DataFrame()

    #for k in range(10):
    for k in range(len(splitted)-1):

        print(k)

        two = IQR_Method(splitted[k])
        iqr_df = pd.concat([iqr_df, two])

        three = iforest(splitted[k])
        ifor_df = pd.concat([ifor_df, three])

        four = oneClassSVM(splitted[k])
        svm_df = pd.concat([svm_df, four])
    lof_df = lof(comb_df)

    iqr_sec = iqrDF(iqr_df)
    lof_sec = lofDF(lof_df)
    ifor_sec = iforDF(ifor_df)
    svm_sec = svmDF(svm_df)
    acual_sec = acualOutlier(comb_df)

    print('iqr-Genauigkeit: ', 100 * accuracy_score(iqr_df['outlier'] == -1, iqr_df['iqr-Outlier'] == -1))
    print('lof-Genauigkeit: ', 100 * accuracy_score(lof_sec['outlier'] == -1, lof_sec['lof-Outlier'] == -1))
    print('ifor-Genauigkeit: ', 100 * accuracy_score(ifor_sec['outlier'] == -1, ifor_sec['ifor-Outlier'] == -1))
    print('svm-Genauigkeit: ', 100 * accuracy_score(svm_sec['outlier'] == -1, svm_sec['svm-Outlier'] == -1))
    temp4 = comb_df.merge(iqr_sec).merge(ifor_sec).merge(lof_sec).merge(svm_sec).merge(acual_sec)
    return temp4


def iqrDF(iqr_df):
    sec = iqr_df.copy()
    conditions = [
        (sec['iqr-Outlier'] <= -1),
        (sec['iqr-Outlier'] >= 1)
    ]
    values = ['an Outlier', 'no Outlier']
    sec['iqr-Class'] = np.select(conditions, values)
    return sec


def iforDF(ifor_df):
    ifor_high = 0.52
    ifor_low = 0.45
    sec = ifor_df.copy()

    ifor_conditions = [
        (sec['ifor-Score'] < ifor_low),
        (sec['ifor-Score'] >= ifor_low) & (sec['ifor-Score'] < ifor_high),
        (sec['ifor-Score'] >= ifor_high)
    ]
    values = ['no Outlier', 'Maybe Outlier', 'an Outlier']
    sec['ifor-Class'] = np.select(ifor_conditions, values)
    return sec


def lofDF(lof_df):
    lof_high = 1.2
    lof_low = 1.05
    sec = lof_df.copy()

    lof_conditions = [
        (sec['lof-Score'] < lof_low),
        (sec['lof-Score'] >= lof_low) & (sec['lof-Score'] < lof_high),
        (sec['lof-Score'] >= lof_high)
    ]
    values = ['no Outlier', 'Maybe Outlier', 'an Outlier']
    sec['lof-Class'] = np.select(lof_conditions, values)

    return sec


def svmDF(svm_df):
    svm_high = 1
    svm_low = -1
    sec = svm_df.copy()

    svm_conditions = [
        (sec['svm-Score'] < svm_low),
        (sec['svm-Score'] >= svm_low) & (sec['svm-Score'] < svm_high),
        (sec['svm-Score'] >= svm_high)
    ]
    values = ['an Outlier', 'Maybe Outlier', 'no Outlier']
    sec['svm-Class'] = np.select(svm_conditions, values)
    return sec


def acualOutlier(comb_df):
    sec = comb_df.copy()
    conditions = [
        (sec['outlier'] == -1),
        (sec['outlier'] == 1)
    ]
    values = ['an Outlier', 'no Outlier']
    sec['actual Outlier'] = np.select(conditions, values)
    return sec




