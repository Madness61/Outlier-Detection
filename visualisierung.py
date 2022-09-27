from matplotlib import pyplot as plt
import pandas as pd


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


# Erstellt 3D Scatterplot von allen Gruppen zusammen.
def visualizeAll3D():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes(projection="3d")

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')
    ax1.set_zlabel('depth', fontweight='bold')

    ax1.scatter(df1.lon, df1.lat, df1.depth, c='blue', label='Group One', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df2.lon, df2.lat, df2.depth, c='orange', label='Group Two', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df3.lon, df3.lat, df3.depth, c='green', label='Group Three', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df4.lon, df4.lat, df4.depth, c='red', label='Group Four', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df5.lon, df5.lat, df5.depth, c='purple', label='Group Five', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df6.lon, df6.lat, df6.depth, c='brown', label='Group Six', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df7.lon, df7.lat, df7.depth, c='pink', label='Group Seven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df8.lon, df8.lat, df8.depth, c='gray', label='Group Eight', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df9.lon, df9.lat, df9.depth, c='olive', label='Group Nine', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df10.lon, df10.lat, df10.depth, c='cyan', label='Group Ten', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df11.lon, df11.lat, df11.depth, c='Black', label='Group Eleven', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    ax1.view_init(10, 190)
    plt.savefig(f'../images/Scatter3DAll.png', dpi=200)


# Erstellt 2D Scatterplot von allen Gruppen zusammen, hier aber der Größe der Gruppe nach sortiert.
def visualAllGroupsSorted():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df7.lon, df7.lat, c='pink', label='Group Seven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df6.lon, df6.lat, c='brown', label='Group Six', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df10.lon, df10.lat, c='cyan', label='Group Ten', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df8.lon, df8.lat, c='gray', label='Group Eight', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df11.lon, df11.lat, c='Black', label='Group Eleven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df9.lon, df9.lat, c='olive', label='Group Nine', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df4.lon, df4.lat, c='red', label='Group Four', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df3.lon, df3.lat, c='green', label='Group Three', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df1.lon, df1.lat, c='blue', label='Group One', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df5.lon, df5.lat, c='purple', label='Group Five', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df2.lon, df2.lat, c='orange', label='Group Two', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    plt.savefig(f'../images/visualAllGroupsSorted.png', dpi=200)


# Erstellt 2D Scatterplot von allen Outliern in allen Gruppen zusammen.
def visualAllOutlierGroupsSorted():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df7.lon[df7['actual Outlier'] == 'an Outlier'], df7.lat[df7['actual Outlier'] == 'an Outlier'], c='pink', label='Group Seven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df6.lon[df6['actual Outlier'] == 'an Outlier'], df6.lat[df6['actual Outlier'] == 'an Outlier'], c='brown', label='Group Six', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df10.lon[df10['actual Outlier'] == 'an Outlier'], df10.lat[df10['actual Outlier'] == 'an Outlier'], c='cyan', label='Group Ten', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df8.lon[df8['actual Outlier'] == 'an Outlier'], df8.lat[df8['actual Outlier'] == 'an Outlier'], c='gray', label='Group Eight', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df11.lon[df11['actual Outlier'] == 'an Outlier'], df11.lat[df11['actual Outlier'] == 'an Outlier'], c='Black', label='Group Eleven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df9.lon[df9['actual Outlier'] == 'an Outlier'], df9.lat[df9['actual Outlier'] == 'an Outlier'], c='olive', label='Group Nine', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df4.lon[df4['actual Outlier'] == 'an Outlier'], df4.lat[df4['actual Outlier'] == 'an Outlier'], c='red', label='Group Four', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df3.lon[df3['actual Outlier'] == 'an Outlier'], df3.lat[df3['actual Outlier'] == 'an Outlier'], c='green', label='Group Three', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df1.lon[df1['actual Outlier'] == 'an Outlier'], df1.lat[df1['actual Outlier'] == 'an Outlier'], c='blue', label='Group One', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df5.lon[df5['actual Outlier'] == 'an Outlier'], df5.lat[df5['actual Outlier'] == 'an Outlier'], c='purple', label='Group Five', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df2.lon[df2['actual Outlier'] == 'an Outlier'], df2.lat[df2['actual Outlier'] == 'an Outlier'], c='orange', label='Group Two', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    plt.savefig(f'../images/visualAllOutlierGroupsSorted.png', dpi=200)


# Erstellt 2D Scatterplot von Gruppe01 bis Gruppe04 zusammen. Der Größe nach sortiert.
def visualGroupsOneToFour():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df4.lon, df4.lat, c='red', label='Group Four', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df3.lon, df3.lat, c='green', label='Group Three', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df1.lon, df1.lat, c='blue', label='Group One', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df2.lon, df2.lat, c='orange', label='Group Two', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    plt.savefig(f'../images/visualGroupsOneToFour.png', dpi=200)


# Erstellt 2D Scatterplot von Gruppe05 bis Gruppe07 zusammen. Der Größe nach sortiert.
def visualGroupsFiveToSeven():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df7.lon, df7.lat, c='pink', label='Group Seven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df6.lon, df6.lat, c='brown', label='Group Six', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df5.lon, df5.lat, c='purple', label='Group Five', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    plt.savefig(f'../images/visualGroupsFiveToSeven.png', dpi=200)


# Erstellt 2D Scatterplot von Gruppe08 bis Gruppe11 zusammen. Der Größe nach sortiert.
def visualGroupsEightToEleven():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df10.lon, df10.lat, c='cyan', label='Group Ten', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df8.lon, df8.lat, c='gray', label='Group Eight', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df11.lon, df11.lat, c='Black', label='Group Eleven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df9.lon, df9.lat, c='olive', label='Group Nine', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    plt.savefig(f'../images/visualGroupsEightToEleven.png', dpi=200)


# Erstellt 2D Scatterplot von Outliern von Gruppe01 bis Gruppe04 zusammen. Der Größe nach sortiert.
def visualOutliersInGroupsOneToFour():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df4.lon[df4['actual Outlier'] == 'an Outlier'], df4.lat[df4['actual Outlier'] == 'an Outlier'], c='red', label='Group Four', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df3.lon[df3['actual Outlier'] == 'an Outlier'], df3.lat[df3['actual Outlier'] == 'an Outlier'], c='green', label='Group Three', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df1.lon[df1['actual Outlier'] == 'an Outlier'], df1.lat[df1['actual Outlier'] == 'an Outlier'], c='blue', label='Group One', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df2.lon[df2['actual Outlier'] == 'an Outlier'], df2.lat[df2['actual Outlier'] == 'an Outlier'], c='orange', label='Group Two', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    plt.savefig(f'../images/visualOutliersInGroupsOneToFour.png', dpi=200)


# Erstellt 2D Scatterplot von Outliern von Gruppe05 bis Gruppe07 zusammen. Der Größe nach sortiert.
def visualOutliersInGroupsFiveToSeven():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df7.lon[df7['actual Outlier'] == 'an Outlier'], df7.lat[df7['actual Outlier'] == 'an Outlier'],
                c='pink', label='Group Seven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df6.lon[df6['actual Outlier'] == 'an Outlier'], df6.lat[df6['actual Outlier'] == 'an Outlier'],
                c='brown', label='Group Six', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df5.lon[df5['actual Outlier'] == 'an Outlier'], df5.lat[df5['actual Outlier'] == 'an Outlier'],
                c='purple', label='Group Five', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)

    plt.savefig(f'../images/visualOutliersInGroupsFiveToSeven.png', dpi=200)


# Erstellt 2D Scatterplot von Outliern von Gruppe08 bis Gruppe11 zusammen. Der Größe nach sortiert.
def visualOutliersInGroupsEightToEleven():
    fig = plt.figure(figsize=(16, 9))
    ax1 = plt.axes()

    ax1.set_xlabel('lon', fontweight='bold')
    ax1.set_ylabel('lat', fontweight='bold')

    ax1.scatter(df10.lon[df10['actual Outlier'] == 'an Outlier'], df10.lat[df10['actual Outlier'] == 'an Outlier'],
                c='cyan', label='Group Ten', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df8.lon[df8['actual Outlier'] == 'an Outlier'], df8.lat[df8['actual Outlier'] == 'an Outlier'],
                c='gray', label='Group Eight', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df11.lon[df11['actual Outlier'] == 'an Outlier'], df11.lat[df11['actual Outlier'] == 'an Outlier'],
                c='Black', label='Group Eleven', s=0.5, alpha=0.1, marker='o')
    ax1.scatter(df9.lon[df9['actual Outlier'] == 'an Outlier'], df9.lat[df9['actual Outlier'] == 'an Outlier'],
                c='olive', label='Group Nine', s=0.5, alpha=0.1, marker='o')

    leg = ax1.legend(loc='best', markerscale=10)
    for lh in leg.legendHandles:
        lh.set_alpha(1)
    plt.savefig(f'../images/visualOutliersInGroupsEightToEleven.png', dpi=200)


# Die Visualisierungen finden gruppenspezifisch statt.
df1 = pd.read_csv('../groups/groupOne.csv')
df1 = clearError(df1)
df2 = pd.read_csv('../groups/groupTwo.csv')
df2 = clearError(df2)
df3 = pd.read_csv('../groups/groupThree.csv')
df3 = clearError(df3)
df4 = pd.read_csv('../groups/groupFour.csv')
df4 = clearError(df4)
df5 = pd.read_csv('../groups/groupFive.csv')
df5 = clearError(df5)
df6 = pd.read_csv('../groups/groupSix.csv')
df6 = clearError(df6)
df7 = pd.read_csv('../groups/groupSeven.csv')
df7 = clearError(df7)
df8 = pd.read_csv('../groups/groupEight.csv')
df8 = clearError(df8)
df9 = pd.read_csv('../groups/groupNine.csv')
df9 = clearError(df9)
df10 = pd.read_csv('../groups/groupTen.csv')
df10 = clearError(df10)
df11 = pd.read_csv('../groups/groupEleven.csv')
df11 = clearError(df11)
