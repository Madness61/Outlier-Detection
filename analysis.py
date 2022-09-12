import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pm4py
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


all = pd.read_csv('../all.csv')


def happyPath():
    #plt.scatter(groupOne['lon'], groupOne['lat'], c='blue')
    #plt.scatter(groupTwo['lon'], groupTwo['lat'], c='red')

    sns.set(style="darkgrid")
    ax1 = plt.subplot(111, projection='3d')
    ax1.set_title('Happy Path')
    ax1.set_xlabel('lon')
    ax1.set_ylabel('lat')
    ax1.set_zlabel('depth')

    for s in groupOne['actual Outlier'].unique():
        if s == 'an Outlier':
            ax1.scatter(groupOne.lon[groupOne['actual Outlier'] == s], groupOne.lat[groupOne['actual Outlier'] == s],
                        groupOne.depth[groupOne['actual Outlier'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax1.scatter(groupOne.lon[groupOne['actual Outlier'] == s], groupOne.lat[groupOne['actual Outlier'] == s],
                        groupOne.depth[groupOne['actual Outlier'] == s], c='cornflowerblue', label=s)

    ax1.legend()
    plt.show()


def AnzahlDerBla():
    df = all.copy()
    df['Right'] = df['Wrong'] = df['Maybe'] = 0

    outlier = df[df['actual Outlier'] == 'an Outlier']
    inliner = df[df['actual Outlier'] == 'no Outlier']

    # df['actual Outlier'] == 'an Outlier'
    # feature guessed correctly
    outlier.loc[outlier['iqr-Class'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['ifor-Class'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['lof-Class'] == 'an Outlier', 'Right'] = outlier['Right'] + 1
    outlier.loc[outlier['svm-Class'] == 'an Outlier', 'Right'] = outlier['Right'] + 1

    # feature guessed maybe
    outlier.loc[df['iqr-Class'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['ifor-Class'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['lof-Class'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1
    outlier.loc[df['svm-Class'] == 'Maybe Outlier', 'Maybe'] = outlier['Maybe'] + 1

    # feature guessed wrong
    outlier.loc[outlier['iqr-Class'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['ifor-Class'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['lof-Class'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1
    outlier.loc[outlier['svm-Class'] == 'no Outlier', 'Wrong'] = outlier['Wrong'] + 1


    # df['actual Outlier'] == 'no Outlier'
    # feature guessed correctly
    inliner.loc[inliner['iqr-Class'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['ifor-Class'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['lof-Class'] == 'no Outlier', 'Right'] = inliner['Right'] + 1
    inliner.loc[inliner['svm-Class'] == 'no Outlier', 'Right'] = inliner['Right'] + 1

    # feature guessed maybe
    inliner.loc[df['iqr-Class'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['ifor-Class'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['lof-Class'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1
    inliner.loc[df['svm-Class'] == 'Maybe Outlier', 'Maybe'] = inliner['Maybe'] + 1

    # feature guessed wrong
    inliner.loc[inliner['iqr-Class'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['ifor-Class'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['lof-Class'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1
    inliner.loc[inliner['svm-Class'] == 'an Outlier', 'Wrong'] = inliner['Wrong'] + 1

    result = outlier.append(inliner)
    return result


def visualize(group):
    ax1 = plt.subplot(231, projection='3d')
    ax1.set_title('Interquartil-Range')
    ax1.set_xlabel('lon')
    ax1.set_ylabel('lat')
    ax1.set_zlabel('depth')

    ax2 = plt.subplot(232, projection='3d')
    ax2.set_title('Isolation Forest')
    ax2.set_xlabel('lon')
    ax2.set_ylabel('lat')
    ax2.set_zlabel('depth')

    ax3 = plt.subplot(233, projection='3d')
    ax3.set_title('Local Outlier Factor')
    ax3.set_xlabel('lon')
    ax3.set_ylabel('lat')
    ax3.set_zlabel('depth')

    ax4 = plt.subplot(234, projection='3d')
    ax4.set_title('One Class Support Vector Machine')
    ax4.set_xlabel('lon')
    ax4.set_ylabel('lat')
    ax4.set_zlabel('depth')

    ax5 = plt.subplot(235, projection='3d')
    ax5.set_title('Actual Data')
    ax5.set_xlabel('lon')
    ax5.set_ylabel('lat')
    ax5.set_zlabel('depth')

    for s in group['iqr-Class'].unique():
        if s == 'an Outlier':
            ax1.scatter(group.lon[group['iqr-Class'] == s], group.lat[group['iqr-Class'] == s], group.depth[group['iqr-Class'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax1.scatter(group.lon[group['iqr-Class'] == s], group.lat[group['iqr-Class'] == s], group.depth[group['iqr-Class'] == s], c='cornflowerblue', label=s)

    for s in group['ifor-Class'].unique():
        if s == 'an Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s], group.depth[group['ifor-Class'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s], group.depth[group['ifor-Class'] == s], c='cornflowerblue', label=s)
        if s == 'Maybe Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s], group.depth[group['ifor-Class'] == s], c='seagreen', label=s)

    for s in group['lof-Class'].unique():
        if s == 'an Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s], group.depth[group['lof-Class'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s], group.depth[group['lof-Class'] == s], c='cornflowerblue', label=s)
        if s == 'Maybe Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s], group.depth[group['lof-Class'] == s], c='seagreen',  label=s)

    for s in group['svm-Class'].unique():
        if s == 'an Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s], group.depth[group['svm-Class'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s], group.depth[group['svm-Class'] == s], c='cornflowerblue', label=s)
        if s == 'Maybe Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s], group.depth[group['svm-Class'] == s], c='seagreen', label=s)

    for s in group['actual Outlier'].unique():
        if s == 'an Outlier':
            ax5.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s], group.depth[group['actual Outlier'] == s], c='crimson', label=s)
        if s == 'no Outlier':
            ax5.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s], group.depth[group['actual Outlier'] == s], c='cornflowerblue', label=s)

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    ax5.legend()
    plt.show()


def evalualteGroup(group):
    outlier = group[group['actual Outlier'] == 'an Outlier']
    inlier = group[group['actual Outlier'] == 'no Outlier']

    iqr_Right = sum(s.count('an Outlier') for s in outlier['iqr-Class']) + sum(s.count('no Outlier') for s in inlier['iqr-Class'])
    iqr_Wrong = sum(s.count('an Outlier') for s in inlier['iqr-Class']) + sum(s.count('no Outlier') for s in outlier['iqr-Class'])

    lof_Right = sum(s.count('an Outlier') for s in outlier['lof-Class']) + sum(s.count('no Outlier') for s in inlier['lof-Class'])
    lof_Wrong = sum(s.count('an Outlier') for s in inlier['lof-Class']) + sum(s.count('no Outlier') for s in outlier['lof-Class'])
    lof_Maybe = sum(s.count('Maybe Outlier') for s in group['lof-Class'])

    ifor_Right = sum(s.count('an Outlier') for s in outlier['ifor-Class']) + sum(s.count('no Outlier') for s in inlier['ifor-Class'])
    ifor_Wrong = sum(s.count('an Outlier') for s in inlier['ifor-Class']) + sum(s.count('no Outlier') for s in outlier['ifor-Class'])
    ifor_Maybe = sum(s.count('Maybe Outlier') for s in group['ifor-Class'])

    svm_Right = sum(s.count('an Outlier') for s in outlier['svm-Class']) + sum(s.count('no Outlier') for s in inlier['svm-Class'])
    svm_Wrong = sum(s.count('an Outlier') for s in inlier['svm-Class']) + sum(s.count('no Outlier') for s in outlier['svm-Class'])
    svm_Maybe = sum(s.count('Maybe Outlier') for s in group['svm-Class'])

    result = pd.DataFrame()
    result.loc[0, 'iqr-Right'] = iqr_Right
    result.loc[0, 'iqr-Wrong'] = iqr_Wrong
    result.loc[0, 'lof-Right'] = lof_Right
    result.loc[0, 'lof-Wrong'] = lof_Wrong
    result.loc[0, 'lof-Maybe'] = lof_Maybe
    result.loc[0, 'ifor-Right'] = ifor_Right
    result.loc[0, 'ifor-Wrong'] = ifor_Wrong
    result.loc[0, 'ifor-Maybe'] = ifor_Maybe
    result.loc[0, 'svm-Right'] = svm_Right
    result.loc[0, 'svm-Wrong'] = svm_Wrong
    result.loc[0, 'svm-Maybe'] = svm_Maybe
    return result


def visualizeCount(group):
    methods = ["IQR", "LOF", "IFor", "SVM"]
    values = {
        "Right": [group._get_value(0, 'iqr-Right').astype(int), group._get_value(0, 'lof-Right').astype(int),
                  group._get_value(0, 'ifor-Right').astype(int), group._get_value(0, 'svm-Right').astype(int)],
        "Wrong": [group._get_value(0, 'iqr-Wrong').astype(int), group._get_value(0, 'lof-Wrong').astype(int),
                  group._get_value(0, 'ifor-Wrong').astype(int), group._get_value(0, 'svm-Wrong').astype(int)],
        "Maybe": [0, group._get_value(0, 'lof-Maybe').astype(int), group._get_value(0, 'ifor-Maybe').astype(int),
                  group._get_value(0, 'svm-Maybe').astype(int)],
    }

    vis = pd.DataFrame(values, index=methods)
    vis.plot(kind="bar", stacked=True, figsize=(10, 8))
    plt.show()


df = AnzahlDerBla()

# 4 Ja Var11,
groupOne = df[df['Right'] == 4]
# 4 Nein Var23
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


three = evalualteGroup(groupOne)
print(three)
happyPath()
#visualize(groupThree)
#visualizeCount(three)

