import pandas as pd
from matplotlib import pyplot as plt
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import loOuFa1
from OneClassSVM import oneClassSVM
from Boxplot import boxplot


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

for k in range(len(splitted)-1):
    print(k)
    print('start', splitted[k])
    one = loOuFa1(splitted[k])
    lof_df = pd.concat([lof_df, one])

    two = IQR_Method(splitted[k])
    iqr_df = pd.concat([iqr_df, two])

    three = iforest(splitted[k])
    ifor_df = pd.concat([ifor_df, three])
    print('end:', splitted[k].columns)
    four = oneClassSVM(splitted[k])
    svm_df = pd.concat([svm_df, four])

# 10,53% richtig
print('LENGTH IQR: ', len(iqr_df.loc[(iqr_df['iqr'] == -1)]))

# 12,77% richtig
print('LENGTH LOF: ', len(lof_df.loc[(lof_df['lof'] == -1)]))

# 31,91% richtig
print('LENGTH IFOREST: ', len(ifor_df.loc[(ifor_df['iforest'] == -1)]))

# 78,17% richtig
print('LENGTH OCSVM: ', len(svm_df.loc[(svm_df['svm'] == -1)]))

print('CORRECT LENGTH: ', len(comb_df.loc[comb_df['outlier'] == -1]))

print(lof_df.columns)
print(iqr_df.columns)
print(ifor_df.columns)
print(svm_df.columns)
print(comb_df.columns)
