import pandas as pd
import pm4py

dataframe = pd.read_csv('../eventlog_expo.csv', nrows=100)
variants = pd.read_csv('../Variants in eventlog.csv', nrows=100)
all = pd.read_csv('../all.csv')

# 4 Ja
groupOne = dataframe[dataframe['Variant index'] == 4]
# 4 Nein
groupTwo = dataframe[(dataframe['Variant index'] == 20) | (dataframe['Variant index'] == 33)]
# 3 Ja 1Nein
groupThree = dataframe[(dataframe['Variant index'] == 5) | (dataframe['Variant index'] == 22) | (dataframe['Variant index'] == 24)]
# 2 Ja 2 Nein
groupFour = dataframe[(dataframe['Variant index'] == 12) | (dataframe['Variant index'] == 29) | (dataframe['Variant index'] == 35) | (dataframe['Variant index'] == 39) | (dataframe['Variant index'] == 48)]
# 1 Ja 3 Nein
groupFive = dataframe[(dataframe['Variant index'] == 15) | (dataframe['Variant index'] == 28) | (dataframe['Variant index'] == 37) | (dataframe['Variant index'] == 49) | (dataframe['Variant index'] == 50)]
# 3 Ja 1 Vielleicht
groupSix = dataframe[(dataframe['Variant index'] == 1) | (dataframe['Variant index'] == 6) | (dataframe['Variant index'] == 14) | (dataframe['Variant index'] == 21)]
# 2 Ja 2 Vielleicht
groupSeven = dataframe[(dataframe['Variant index'] == 2) | (dataframe['Variant index'] == 7) | (dataframe['Variant index'] == 13) | (dataframe['Variant index'] == 16) | (dataframe['Variant index'] == 41)]
# 1 Ja 3 Vielleicht
groupEight = dataframe[(dataframe['Variant index'] == 9) | (dataframe['Variant index'] == 32)]
# 3 Nein 1 Vielleicht
groupNine = dataframe[(dataframe['Variant index'] == 36) | (dataframe['Variant index'] == 42) | (dataframe['Variant index'] == 51)]
# 2 Nein 2 Vielleicht
groupTen = dataframe[(dataframe['Variant index'] == 34)]
# groupEleven


def evaluate(group):
    merge = pd.merge(group, variants, on='Variant', how='inner')
    eval = merge[['Case ID', 'Variant index', 'Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5']]
    filtered = eval.drop_duplicates()
    filtered.to_csv('../filtered.csv')
    return filtered


six = evaluate(groupSix)
print(six)

