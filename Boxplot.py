import seaborn as sns
import matplotlib.pyplot as plt
from readFile import df


def boxplot(column):
    sns.boxplot(data=df, x=df[f"{column}"])
    plt.title(f"Boxplot of coordinate  {column}")
    plt.show()


boxplot('x')
boxplot('y')
boxplot('z')
