import pandas as pd
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import lof
from OneClassSVM import oneClassSVM
import numpy as np


# Aufteilen des Datensatzes in Chunks. Hierbei kann die Chunkgröße individuell gewählt werden.
def split_dataframe(df, chunk_size):
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks


def calcFeature(comb_df):
    # Teilt den Datensatz in chunks der Größe 1000
    splitted = split_dataframe(comb_df, 1000)
    iqr_df = pd.DataFrame()
    ifor_df = pd.DataFrame()
    svm_df = pd.DataFrame()

    # Iteriert durch die Anzahl der durch Splitted generierten "1000er Blöcke".
    for k in range(len(splitted)-1):
        # Anwenden der IQR-Methode auf Chunk und anschließend zu dataframe zusammengefügt.
        tmp = IQR_Method(splitted[k])
        iqr_df = pd.concat([iqr_df, tmp])

        # Anwenden der Isolation Forest-Methode auf Chunk und anschließend zu dataframe zusammengefügt.
        tmp = iforest(splitted[k])
        ifor_df = pd.concat([ifor_df, tmp])

        # Anwenden der OC-SVM-Methode auf Chunk und anschließend zu dataframe zusammengefügt.
        tmp = oneClassSVM(splitted[k])
        svm_df = pd.concat([svm_df, tmp])

    # Da LOF lokale Anomalien bereits betrachtet, kann es auf den gesamten Daten arbeiten.
    lof_df = lof(comb_df)

    # Aufruf für Klassifizierungen (an / no / maybe).
    iqr_sec = iqrDF(iqr_df)
    lof_sec = lofDF(lof_df)
    ifor_sec = iforDF(ifor_df)
    svm_sec = svmDF(svm_df)
    acual_sec = acualOutlier(comb_df)

    # Zusammenfügen der Methodenergebnisse.
    result = comb_df.merge(iqr_sec).merge(ifor_sec).merge(lof_sec).merge(svm_sec).merge(acual_sec)
    return result


# Funktion klassifiziert IQR. Hier gibt es kein "Maybe".
def iqrDF(iqr_df):
    sec = iqr_df.copy()
    conditions = [
        (sec['iqr-Outlier'] <= -1),
        (sec['iqr-Outlier'] >= 1)
    ]
    values = ['an Outlier', 'no Outlier']
    sec['iqr-Class'] = np.select(conditions, values)
    return sec


# Funktion klassifiziert Isolation Forest. Schranken wurden zwischen 0.45 und 0.52 gesetzt,
# da ansonsten 95% maybe wären.
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


# Funktion klassifiziert LOF. Schranken wurden als 1.05 und 1.2 gewählt.
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


# Funktion klassifiziert OC-SVM. Schranken sind hier -1 und 1.
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


# Funktion klassifiziert tatsächliches Ergebnis. Ist nur visuell, damit im Prozessmodell nicht -1 / 1 steht.
def acualOutlier(comb_df):
    sec = comb_df.copy()
    conditions = [
        (sec['outlier'] == -1),
        (sec['outlier'] == 1)
    ]
    values = ['an Outlier', 'no Outlier']
    sec['actual Outlier'] = np.select(conditions, values)
    return sec
