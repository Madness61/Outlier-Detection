import os
import pandas as pd


# Durchläuft jede Datei, die nach Aufruf von main.py generiert wurde.
# Wertet jeden Datenpunkt aus und summiert die Anzahl an richtig / falsch / vielleicht liegen der Methode.
# Anschließend werden die Gruppen erzeugt und abgespeichert.
path = '../result/'
for file in os.listdir(path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(path, file))
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
        result.to_csv("../resultWithCounts.csv", index=False, header=('0', '1', 'index', 'lon', 'lat', 'depth', 'outlier','iqr-Outlier','iqr-Class','ifor-Outlier','ifor-Score','ifor-Class','lof-Score','lof-Outlier','lof-Class','svm-Score','svm-Outlier','svm-Class','actual Outlier', 'Right' , 'Wrong', 'Maybe'), mode='a')

        groupOne = groupTwo = groupThree = groupFour = groupFive = groupSix = groupSeven = groupEight = groupNine = \
            groupTen = groupEleven = pd.DataFrame(columns=('0', '1', 'index', 'lon', 'lat', 'depth', 'outlier',
                                                           'iqr-Outlier', 'iqr-Class', 'ifor-Outlier', 'ifor-Score',
                                                           'ifor-Class', 'lof-Score', 'lof-Outlier', 'lof-Class',
                                                           'svm-Score', 'svm-Outlier', 'svm-Class', 'actual Outlier',
                                                           'Right', 'Wrong', 'Maybe'))
        # 4 Ja
        groupOne = result[result['Right'] == 4]
        groupOne.reset_index(drop=True, inplace=True)
        groupOne.to_csv('../groups/groupOne.csv', index=False, mode='a')
        types = groupOne.applymap(type)
        # 4 Nein
        groupTwo = result[result['Wrong'] == 4]
        groupTwo.reset_index(drop=True, inplace=True)
        groupTwo.to_csv('../groups/groupTwo.csv', index=False, mode='a')
        # 3 Ja 1 Nein
        groupThree = result[(result['Right'] == 3) & (result['Wrong'] == 1)]
        groupThree.reset_index(drop=True, inplace=True)
        groupThree.to_csv('../groups/groupThree.csv', index=False, mode='a')
        # 2 Ja 2 Nein
        groupFour = result[(result['Right'] == 2) & (result['Wrong'] == 2)]
        groupFour.reset_index(drop=True, inplace=True)
        groupFour.to_csv('../groups/groupFour.csv', index=False, mode='a')
        # 1 Ja 3 Nein
        groupFive = result[(result['Right'] == 1) & (result['Wrong'] == 3)]
        groupFive.reset_index(drop=True, inplace=True)
        groupFive.to_csv('../groups/groupFive.csv', index=False, mode='a')
        # 3 Ja 1 Vielleicht
        groupSix = result[(result['Right'] == 3) & (result['Maybe'] == 1)]
        groupSix.reset_index(drop=True, inplace=True)
        groupSix.to_csv('../groups/groupSix.csv', index=False, mode='a')
        # 2 Ja 2 Vielleicht
        groupSeven = result[(result['Right'] == 2) & (result['Maybe'] == 2)]
        groupSeven.reset_index(drop=True, inplace=True)
        groupSeven.to_csv('../groups/groupSeven.csv', index=False, mode='a')
        # 1 Ja 3 Vielleicht
        groupEight = result[(result['Right'] == 1) & (result['Maybe'] == 3)]
        groupEight.reset_index(drop=True, inplace=True)
        groupEight.to_csv('../groups/groupEight.csv', index=False, mode='a')
        # 3 Nein 1 Vielleicht
        groupNine = result[(result['Wrong'] == 3) & (result['Maybe'] == 1)]
        groupNine.reset_index(drop=True, inplace=True)
        groupNine.to_csv('../groups/groupNine.csv', index=False, mode='a')
        # 2 Nein 2 Vielleicht
        groupTen = result[(result['Wrong'] == 2) & (result['Maybe'] == 2)]
        groupTen.reset_index(drop=True, inplace=True)
        groupTen.to_csv('../groups/groupTen.csv', index=False, mode='a')
        # 1 Nein 3 Vielleicht
        groupEleven = result[(result['Wrong'] == 1) & (result['Maybe'] == 3)]
        groupEleven.reset_index(drop=True, inplace=True)
        groupEleven.to_csv('../groups/groupEleven.csv', index=False, mode='a')
