import pandas as pd
from IQR_Method import IQR_Method
from isolation_forest import iforest, backup
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
    lof_df = pd.DataFrame()
    iqr_df = pd.DataFrame()
    ifor_df = pd.DataFrame()
    svm_df = pd.DataFrame()

    #for k in range(10):
    for k in range(len(splitted)-1):
        # for filename in os.scandir('result'):
        #    print(pd.read_feather(filename))
        #    k = pd.read_feather(filename)
        print(k)
        one = lof(splitted[k])
        lof_df = pd.concat([lof_df, one])

        two = IQR_Method(splitted[k])
        iqr_df = pd.concat([iqr_df, two])

        three = backup(splitted[k])
        ifor_df = pd.concat([ifor_df, three])

        four = oneClassSVM(splitted[k])
        svm_df = pd.concat([svm_df, four])

    iqr_sec = iqrDF(iqr_df)
    ifor_sec = iforDF(ifor_df)
    lof_sec = lofDF(lof_df)
    svm_sec = svmDF(svm_df)
    acual_sec = acualOutlier(comb_df)

    print('iqr-Genauigkeit: ', 100 * accuracy_score(iqr_df['outlier'] == -1, iqr_df['iqr-Outlier'] == -1))
    print('ifor-Genauigkeit: ', 100 * accuracy_score(iqr_df['outlier'] == -1, ifor_sec['ifor-Outlier'] == -1))
    print('lof-Genauigkeit: ', 100 * accuracy_score(iqr_df['outlier'] == -1, lof_sec['lof-Outlier'] == -1))
    print('svm-Genauigkeit: ', 100 * accuracy_score(iqr_df['outlier'] == -1, svm_sec['ocsvm-Outlier'] == -1))
    temp4 = iqr_sec.join(ifor_sec).join(lof_sec).join(svm_sec).join(acual_sec)
    return temp4


def iqrDF(iqr_df):
    sec = iqr_df[['iqr-Outlier']].copy()
    conditions = [
        (sec['iqr-Outlier'] <= -1),
        (sec['iqr-Outlier'] >= 1)
    ]
    values = ['Likely no Outlier', 'Likely an Outlier']
    sec['iqr-Prob'] = np.select(conditions, values)
    return sec


def iforDF(ifor_df):
    ifor_high = 0.2
    ifor_low = -0.2
    sec = ifor_df[['ifor-Score', 'ifor-Outlier']].copy()

    ifor_conditions = [
        (sec['ifor-Score'] < ifor_low),
        (sec['ifor-Score'] >= ifor_low) & (sec['ifor-Score'] < ifor_high),
        (sec['ifor-Score'] >= ifor_high)
    ]
    values = ['Likely no Outlier', 'Maybe Outlier', 'Likely an Outlier']
    sec['ifor-Prob'] = np.select(ifor_conditions, values)
    return sec


def lofDF(lof_df):
    lof_high = 1.2
    lof_low = 1
    sec = lof_df[['lof-Score', 'lof-Outlier']].copy()

    lof_conditions = [
        (sec['lof-Score'] < lof_low),
        (sec['lof-Score'] >= lof_low) & (sec['lof-Score'] < lof_high),
        (sec['lof-Score'] >= lof_high)
    ]
    values = ['Likely no Outlier', 'Maybe Outlier', 'Likely an Outlier']
    sec['lof-Prob'] = np.select(lof_conditions, values)

    return sec


def svmDF(svm_df):
    svm_high, svm_low = np.percentile(svm_df['ocsvm-Score'], [66, 33])
    sec = svm_df[['ocsvm-Score', 'ocsvm-Outlier']].copy()

    svm_conditions = [
        (sec['ocsvm-Score'] < svm_low),
        (sec['ocsvm-Score'] >= svm_low) & (sec['ocsvm-Score'] < svm_high),
        (sec['ocsvm-Score'] >= svm_high)
    ]
    values = ['likely no Outlier', 'Maybe Outlier', 'Likely an Outlier']
    sec['svm-Prob'] = np.select(svm_conditions, values)
    return sec


def acualOutlier(comb_df):
    sec = comb_df[['outlier']].copy()
    conditions = [
        (sec['outlier'] <= -1),
        (sec['outlier'] >= 1)
    ]
    values = [' no Outlier', ' an Outlier']
    sec['actual Outlier'] = np.select(conditions, values)
    return sec




