import pandas as pd
import matplotlib.pyplot as plt


# Funktion erstellt 3D Scatterplot für jeden der 4 Methoden und 1 für die tatsächlichen Daten
def visualize(group, name):
    fig = plt.figure(figsize=(16, 9))

    ax1 = plt.subplot(231, projection='3d')
    ax1.view_init(10, 190)
    ax1.set_title('Interquartil-Range')
    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')
    ax1.set_zlabel('depth', fontweight='bold')

    ax2 = plt.subplot(232, projection='3d')
    ax2.view_init(10, 190)
    ax2.set_title('Isolation Forest')
    ax2.set_xlabel('lon', fontweight='bold')
    ax2.set_ylabel('lat', fontweight='bold')
    ax2.set_zlabel('depth', fontweight='bold')

    ax3 = plt.subplot(234, projection='3d')
    ax3.view_init(10, 190)
    ax3.set_title('Local Outlier Factor')
    ax3.set_xlabel('lon', fontweight='bold')
    ax3.set_ylabel('lat', fontweight='bold')
    ax3.set_zlabel('depth', fontweight='bold')

    ax4 = plt.subplot(235, projection='3d')
    ax4.view_init(10, 190)
    ax4.set_title('One Class Support Vector Machine')
    ax4.set_xlabel('lon', fontweight='bold')
    ax4.set_ylabel('lat', fontweight='bold')
    ax4.set_zlabel('depth', fontweight='bold')

    ax5 = plt.subplot(233, projection='3d')
    ax5.view_init(10, 190)
    ax5.set_title('Actual Data')
    ax5.set_xlabel('lon', fontweight='bold')
    ax5.set_ylabel('lat', fontweight='bold')
    ax5.set_zlabel('depth', fontweight='bold')

    for s in group['iqr-Class'].unique():
        if s == 'an Outlier':
            ax1.scatter(group.lon[group['iqr-Class'] == s], group.lat[group['iqr-Class'] == s],
                        group.depth[group['iqr-Class'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax1.scatter(group.lon[group['iqr-Class'] == s], group.lat[group['iqr-Class'] == s],
                        group.depth[group['iqr-Class'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)

    for s in group['ifor-Class'].unique():
        if s == 'an Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s],
                        group.depth[group['ifor-Class'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s],
                        group.depth[group['ifor-Class'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)
        if s == 'Maybe Outlier':
            ax2.scatter(group.lon[group['ifor-Class'] == s], group.lat[group['ifor-Class'] == s],
                        group.depth[group['ifor-Class'] == s], c='seagreen', label=s, s=0.5, alpha=0.1)

    for s in group['lof-Class'].unique():
        if s == 'an Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s],
                        group.depth[group['lof-Class'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s],
                        group.depth[group['lof-Class'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)
        if s == 'Maybe Outlier':
            ax3.scatter(group.lon[group['lof-Class'] == s], group.lat[group['lof-Class'] == s],
                        group.depth[group['lof-Class'] == s], c='seagreen', label=s, s=0.5, alpha=0.1)

    for s in group['svm-Class'].unique():
        if s == 'an Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s],
                        group.depth[group['svm-Class'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s],
                        group.depth[group['svm-Class'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)
        if s == 'Maybe Outlier':
            ax4.scatter(group.lon[group['svm-Class'] == s], group.lat[group['svm-Class'] == s],
                        group.depth[group['svm-Class'] == s], c='seagreen', label=s, s=0.5, alpha=0.1)

    for s in group['actual Outlier'].unique():
        if s == 'an Outlier':
            ax5.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s],
                        group.depth[group['actual Outlier'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax5.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s],
                        group.depth[group['actual Outlier'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)

    leg = ax1.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    leg = ax2.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    leg = ax3.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    leg = ax4.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    leg = ax5.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    #plt.savefig(f'../images/ScatterGroup{name}.png', dpi=200)
    plt.show()


# Funktion zählt die Anzahl an richtig, falsch und vielleicht gelegenen Vorkommnisse in der Gruppe
def evalualteGroup(group):
    outlier = group[group['actual Outlier'] == 'an Outlier']
    inlier = group[group['actual Outlier'] == 'no Outlier']

    iqr_Right = int(sum(s.count('an Outlier') for s in outlier['iqr-Class']) + sum(
        s.count('no Outlier') for s in inlier['iqr-Class']))
    iqr_Wrong = int(sum(s.count('an Outlier') for s in inlier['iqr-Class']) + sum(
        s.count('no Outlier') for s in outlier['iqr-Class']))

    lof_Right = int(sum(s.count('an Outlier') for s in outlier['lof-Class']) + sum(
        s.count('no Outlier') for s in inlier['lof-Class']))
    lof_Wrong = int(sum(s.count('an Outlier') for s in inlier['lof-Class']) + sum(
        s.count('no Outlier') for s in outlier['lof-Class']))
    lof_Maybe = int(sum(s.count('Maybe Outlier') for s in group['lof-Class']))

    ifor_Right = int(sum(s.count('an Outlier') for s in outlier['ifor-Class']) + sum(
        s.count('no Outlier') for s in inlier['ifor-Class']))
    ifor_Wrong = int(sum(s.count('an Outlier') for s in inlier['ifor-Class']) + sum(
        s.count('no Outlier') for s in outlier['ifor-Class']))
    ifor_Maybe = int(sum(s.count('Maybe Outlier') for s in group['ifor-Class']))

    svm_Right = int(sum(s.count('an Outlier') for s in outlier['svm-Class']) + sum(
        s.count('no Outlier') for s in inlier['svm-Class']))
    svm_Wrong = int(sum(s.count('an Outlier') for s in inlier['svm-Class']) + sum(
        s.count('no Outlier') for s in outlier['svm-Class']))
    svm_Maybe = int(sum(s.count('Maybe Outlier') for s in group['svm-Class']))

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


# Speichert Barplot, welcher Richtigkeit der Methoden der Gruppe ausdrückt
def visualizeCount(group, name):
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
    vis.plot(kind="bar", stacked=True, figsize=(16, 9))
    #plt.savefig(f'../images/Count{name}.png', dpi=200)
    plt.show()

# Musste eingefügt werden, weil der Datensatz unterschiedliche typen hat. Transformiert Strings also zurück zu
# numerischen Zahlen
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


# 3D Plot der tatsächlichen Daten der übergebenen Gruppe.
def single(group, name):
    ax1 = plt.axes(projection="3d")

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')
    ax1.set_zlabel('depth', fontweight='bold')

    for s in group['actual Outlier'].unique():
        if s == 'an Outlier':
            ax1.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s], group.depth[group['actual Outlier'] == s], c='crimson', label=s, s=0.5, alpha=0.1)
        if s == 'no Outlier':
            ax1.scatter(group.lon[group['actual Outlier'] == s], group.lat[group['actual Outlier'] == s], group.depth[group['actual Outlier'] == s], c='cornflowerblue', label=s, s=0.5, alpha=0.1)

    # Legendenposition oben links
    leg = ax1.legend(loc='lower left', bbox_to_anchor=(0.7, 0.7), markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    ax1.view_init(10, 190)
    plt.savefig(f'../images/ScatterGroup{name}.png', dpi=200)


df = pd.read_csv('../groups/groupThree.csv')
df = clearError(df)
eval = evalualteGroup(df)
visualizeCount(eval, 'Three')
#visualize(df, 'Three')