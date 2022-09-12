import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df):
    sns.set(style='whitegrid')
    df = sns.load_dataset("titanic")
    sns.boxplot(x=df["age"])
    plt.show()
