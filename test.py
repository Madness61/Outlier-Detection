import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from Boxplot import boxplot


def split_dataframe(bla, chunk_size):
    chunks = list()
    num_chunks = len(bla) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(bla[i * chunk_size:(i + 1) * chunk_size])
    return chunks


comb_df = pd.read_feather('together_combined.feather')
all_df = pd.read_csv('../all.csv')
outlier = comb_df[comb_df['outlier'] == -1]
splitted = split_dataframe(all_df, 1000)

sns.set(style='whitegrid')
sns.scatterplot(data=splitted[10], x='lon', y='lat', hue='outlier',palette="deep")

plt.show()




