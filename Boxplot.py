import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df, column):
    sns.boxplot(data=df, x=df[f"{column}"])
    plt.title(f"Boxplot of coordinate  {column} with index between {df.index.start} and {df.index.stop-1}")
    plt.show()


