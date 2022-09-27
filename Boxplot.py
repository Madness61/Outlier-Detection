import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Siehe Erklärung in visualizePlots().
def clearError(dataframe):
    dataframe['index'] = pd.to_numeric(dataframe['index'], errors='coerce')
    dataframe['lon'] = pd.to_numeric(dataframe['lon'], errors='coerce')
    dataframe['lat'] = pd.to_numeric(dataframe['lat'], errors='coerce')
    dataframe['depth'] = pd.to_numeric(dataframe['depth'], errors='coerce')
    dataframe['outlier'] = pd.to_numeric(dataframe['outlier'], errors='coerce')
    dataframe['iqr-Outlier'] = pd.to_numeric(dataframe['iqr-Outlier'], errors='coerce')
    dataframe['ifor-Outlier'] = pd.to_numeric(dataframe['ifor-Outlier'], errors='coerce')
    dataframe['ifor-Score'] = pd.to_numeric(dataframe['ifor-Score'], errors='coerce')
    dataframe['lof-Score'] = pd.to_numeric(dataframe['lof-Score'], errors='coerce')
    dataframe['lof-Outlier'] = pd.to_numeric(dataframe['lof-Outlier'], errors='coerce')
    dataframe['svm-Score'] = pd.to_numeric(dataframe['svm-Score'], errors='coerce')
    dataframe['Right'] = pd.to_numeric(dataframe['Right'], errors='coerce')
    dataframe['Wrong'] = pd.to_numeric(dataframe['Wrong'], errors='coerce')
    dataframe['Maybe'] = pd.to_numeric(dataframe['Maybe'], errors='coerce')
    return dataframe


# Erstellt mithilfe von seabron einen Boxplot.
def boxplot():
    tips = sns.load_dataset("tips")
    sns.boxplot(y="total_bill", data=tips)
    plt.show()


