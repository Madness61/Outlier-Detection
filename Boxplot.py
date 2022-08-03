import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df, column):
    sns.boxplot(data=df, x=df[f"{column}"])
    plt.title(f"Boxplot of coordinate  {column}")
    plt.show()


