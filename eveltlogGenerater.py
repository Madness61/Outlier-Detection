import pandas as pd
from matplotlib import pyplot as plt
from IQR_Method import IQR_Method
from isolation_forest import iforest
from LOF_Method import loOuFa1
from OneClassSVM import oneClassSVM
from Boxplot import boxplot
import numpy as np
import datetime as dt

comb_df = pd.read_feather('together_combined.feather')
all_df = pd.read_csv('all.csv')

eventlog = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])

x = comb_df['x'].astype(str)
y = comb_df['y'].astype(str)
z = comb_df['z'].astype(str)


el_lof = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
el_ifor = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
el_svm = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
el_iqr = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])

# Case ID: concat the strings.
el_lof['CaseID'] = x + " " + y + " " + z
el_ifor['CaseID'] = x + " " + y + " " + z
el_svm['CaseID'] = x + " " + y + " " + z
el_iqr['CaseID'] = x + " " + y + " " + z

# Activity:
el_lof['Activity'] = 'LOF: ' + all_df['lof-Prob'].astype(str)
el_ifor['Activity'] = 'Iforest: ' + all_df['ifor-Prob'].astype(str)
el_svm['Activity'] = 'SVM: ' + all_df['svm-Prob'].astype(str)
el_iqr['Activity'] = 'IQR: ' + all_df['iqr-Prob'].astype(str)

# Resource:
el_lof['Resource'] = 'LOF: ' + all_df['lof-Score'].astype(str)
el_ifor['Resource'] = 'Iforest: ' + all_df['ifor-Score'].astype(str)
el_svm['Resource'] = 'SVM: ' + all_df['ocsvm-Score'].astype(str)
el_iqr['Resource'] = 'IQR: ' + all_df['iqr-Outlier'].astype(str)

eventlog = el_iqr.append(el_lof).append(el_ifor).append(el_svm)
eventlog.reset_index(inplace=True)

# For Timestamp
startdate = dt.datetime(1900, 1, 1, 0, 0, 0)
for index, row in eventlog.iterrows():
    print(index)
    eventlog['Timestamp'][index] = startdate + dt.timedelta(seconds=index)

eventlog.drop('index', axis=1)
eventlog.to_csv('eventlog.csv')
print(eventlog)
