import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pm4py
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

dataframe = pd.read_csv('../eventlog_expo.csv', nrows=100)
cases = pd.read_csv('../Cases in eventlog.csv')
variant = pd.read_csv('../Variants in eventlog.csv')
all = pd.read_csv('../all.csv')
comb = pd.read_feather('together_combined.feather')

def happyPath():
    #plt.scatter(groupOne['x'], groupOne['y'], c='blue')
    #plt.scatter(groupTwo['x'], groupTwo['y'], c='red')

    sns.set(style="darkgrid")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(groupOne['x'], groupOne['y'], groupOne['z'], s=40, c='b', marker='o')
    ax.scatter(groupTwo['x'], groupTwo['y'], groupTwo['z'], s=40, c='r', marker='^')
    plt.show()


def AnzahlDerBla():
    df = all.copy()
    df['Right'] = 0
    df['Wrong'] = 0
    df['Maybe'] = 0

    outlier = df[df['actual Outlier'] == 'an Outlier']
    inliner = df[df['actual Outlier'] == 'no Outlier']



    # df['actual Outlier'] == 'an Outlier'
    # feature guessed correctly
    outlier.loc[outlier['iqr-Prob'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['ifor-Prob'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['lof-Prob'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['svm-Prob'] == 'an Outlier', 'Right'] = outlier['Right'] + 1

    # feature guessed maybe
    outlier.loc[df['iqr-Prob'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['ifor-Prob'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['lof-Prob'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['svm-Prob'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1

    # feature guessed wrong
    outlier.loc[outlier['iqr-Prob'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['ifor-Prob'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['lof-Prob'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['svm-Prob'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1


    # df['actual Outlier'] == 'no Outlier'
    # feature guessed correctly
    inliner.loc[inliner['iqr-Prob'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['ifor-Prob'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['lof-Prob'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['svm-Prob'] == 'no Outlier', 'Right'] = inliner['Right'] + 1

    # feature guessed maybe
    inliner.loc[df['iqr-Prob'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['ifor-Prob'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['lof-Prob'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['svm-Prob'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1

    # feature guessed wrong
    inliner.loc[inliner['iqr-Prob'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['ifor-Prob'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['lof-Prob'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['svm-Prob'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1

    result = outlier.append(inliner)
    return result


def visualizeAll():
    plt.scatter(groupOne['x'], groupOne['y'], marker='o')
    plt.scatter(groupTwo['x'], groupTwo['y'], marker='x')
    plt.scatter(groupThree['x'], groupThree['y'], marker='*')
    plt.scatter(groupFour['x'], groupFour['y'], marker='+')
    plt.scatter(groupFive['x'], groupFive['y'], marker='s')
    plt.scatter(groupSix['x'], groupSix['y'], marker='<')
    plt.scatter(groupSeven['x'], groupSeven['y'], marker='>')
    plt.show()


df = AnzahlDerBla()

# 4 Ja
groupOne = df[df['Right'] == 4]
# 4 Nein
groupTwo = df[df['Wrong'] == 4]
# 3 Ja 1 Nein
groupThree = df[(df['Right'] == 3) & (df['Wrong'] == 1)]
# 2 Ja 2 Nein
groupFour = df[(df['Right'] == 2) & (df['Wrong'] == 2)]
# 1 Ja 3 Nein
groupFive = df[(df['Right'] == 1) & (df['Wrong'] == 3)]
# 3 Ja 1 Vielleicht
groupSix = df[(df['Right'] == 3) & (df['Maybe'] == 1)]
# 2 Ja 2 Vielleicht
groupSeven = df[(df['Right'] == 2) & (df['Maybe'] == 2)]
# 1 Ja 3 Vielleicht
groupEight = df[(df['Right'] == 1) & (df['Maybe'] == 3)]
# 3 Nein 1 Vielleicht
groupNine = df[(df['Wrong'] == 3) & (df['Maybe'] == 1)]
# 2 Nein 2 Vielleicht
groupTen = df[(df['Wrong'] == 2) & (df['Maybe'] == 2)]
# 1 Nein 3 Vielleicht
groupEleven = df[(df['Wrong'] == 1) & (df['Maybe'] == 3)]

happyPath()
visualizeAll()




