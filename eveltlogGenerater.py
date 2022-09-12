import pandas as pd
import datetime as dt


def getEventlog(comb_df, all_df):
    #comb_df = pd.read_feather('together_combined.feather')
    #all_df = pd.read_csv('../all.csv')

    x = comb_df['lon'].astype(str)
    y = comb_df['lat'].astype(str)
    z = comb_df['depth'].astype(str)

    el_lof = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
    el_ifor = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
    el_svm = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
    el_iqr = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])
    el_actual = pd.DataFrame(columns=['CaseID', 'Timestamp', 'Activity', 'Resource'])

    # Case ID: concat the strings.
    el_lof['CaseID'] = x + " " + y + " " + z
    el_ifor['CaseID'] = x + " " + y + " " + z
    el_svm['CaseID'] = x + " " + y + " " + z
    el_iqr['CaseID'] = x + " " + y + " " + z
    el_actual['CaseID'] = x + " " + y + " " + z

    # Activity:
    el_lof['Activity'] = 'LOF: ' + all_df['lof-Class'].astype(str)
    el_ifor['Activity'] = 'Iforest: ' + all_df['ifor-Class'].astype(str)
    el_svm['Activity'] = 'SVM: ' + all_df['svm-Class'].astype(str)
    el_iqr['Activity'] = 'IQR: ' + all_df['iqr-Class'].astype(str)
    el_actual['Activity'] = all_df['actual Outlier'].astype(str)

    # Resource:
    el_lof['Resource'] = 'LOF: ' + all_df['lof-Score'].astype(str)
    el_ifor['Resource'] = 'Iforest: ' + all_df['ifor-Score'].astype(str)
    el_svm['Resource'] = 'SVM: ' + all_df['svm-Score'].astype(str)
    el_iqr['Resource'] = 'IQR: ' + all_df['iqr-Outlier'].astype(str)
    el_actual['Resource'] = 'actual Outlier: ' + all_df['outlier'].astype(str)

    eventlog = el_iqr.append(el_lof).append(el_ifor).append(el_svm).append(el_actual)

    # For Timestamp
    startdate = dt.datetime(2000, 1, 1, 0, 0, 0)
    eventlog['Timestamp'] = pd.date_range(startdate, periods=len(eventlog), freq='1S')

    #eventlog = eventlog.sort_values(by=['CaseID'])
    eventlog.reset_index(inplace=True)
    return eventlog
