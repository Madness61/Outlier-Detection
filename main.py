import pandas as pd
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import loOuFa1
from OneClassSVM import oneClassSVM
from Boxplot import boxplot
import numpy as np


def split_dataframe(df, chunk_size):
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks


# 82247180 Zeilen in raw1.xyz
raw_df = pd.read_feather('raw.feather')
comb_df = pd.read_feather('together_combined.feather')

splitted = split_dataframe(comb_df, 1000)

lof_df = pd.DataFrame()
iqr_df = pd.DataFrame()
ifor_df = pd.DataFrame()
svm_df = pd.DataFrame()

#for k in range(5):
for k in range(len(splitted)-1):
    print(k)
    one = loOuFa1(splitted[k])
    lof_df = pd.concat([lof_df, one])

    two = IQR_Method(splitted[k])
    iqr_df = pd.concat([iqr_df, two])

    three = iforest(splitted[k])
    ifor_df = pd.concat([ifor_df, three])

    four = oneClassSVM(splitted[k])
    svm_df = pd.concat([svm_df, four])


def iqrDF():
    sec = iqr_df[['iqr-Outlier']].copy()
    conditions = [
        (sec['iqr-Outlier'] <= -1),
        (sec['iqr-Outlier'] >= 1)
    ]
    values = ['Likely no Outlier', 'Likely an Outlier']
    sec['iqr-Prob'] = np.select(conditions, values)
    return sec


def iforDF():
    ifor_high, ifor_low = np.percentile(ifor_df['ifor-Score'], [66, 33])
    sec = ifor_df[['ifor-Score', 'ifor-Outlier']].copy()

    ifor_conditions = [
        (sec['ifor-Score'] < ifor_low),
        (sec['ifor-Score'] >= ifor_low) & (sec['ifor-Score'] < ifor_high),
        (sec['ifor-Score'] >= ifor_high)
    ]
    values = ['Likely no Outlier', 'Maybe Outlier', 'Likely an Outlier']
    sec['ifor-Prob'] = np.select(ifor_conditions, values)

    return sec


def lofDF():
    lof_high, lof_low = np.percentile(lof_df['lof-Score'], [66, 33])
    sec = lof_df[['lof-Score', 'lof-Outlier']].copy()

    lof_conditions = [
        (sec['lof-Score'] < lof_low),
        (sec['lof-Score'] >= lof_low) & (sec['lof-Score'] < lof_high),
        (sec['lof-Score'] >= lof_high)
    ]
    values = ['Likely no Outlier', 'Maybe Outlier', 'Likely an Outlier']
    sec['lof-Prob'] = np.select(lof_conditions, values)

    return sec


def svmDF():
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


iqr_sec = iqrDF()
ifor_sec = iforDF()
lof_sec = lofDF()
svm_sec = svmDF()

temp4 = iqr_sec.join(ifor_sec).join(lof_sec).join(svm_sec)
temp4.to_csv('all.csv')
