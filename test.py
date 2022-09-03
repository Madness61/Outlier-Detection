import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import where
from sklearn import preprocessing, __all__, svm
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC, OneClassSVM
from seaborn import load_dataset, pairplot
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def split_dataframe(bla, chunk_size):
    chunks = list()
    num_chunks = len(bla) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(bla[i * chunk_size:(i + 1) * chunk_size])
    return chunks


comb_df = pd.read_feather('together_combined.feather')
splitted = split_dataframe(comb_df, 100)


df = splitted[0]

X = df[['z']]
y = df['outlier']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

column_transformer = make_column_transformer(
    (StandardScaler(), ['z']),
    remainder='passthrough')

X_train = column_transformer.fit_transform(X_train)
X_train = pd.DataFrame(data=X_train, columns=column_transformer.get_feature_names_out())
clf = SVC(kernel='rbf', gamma=0.01, C=1000)
clf.fit(X_train, y_train)

X_test = column_transformer.transform(X_test)
X_test = pd.DataFrame(data=X_test, columns=column_transformer.get_feature_names_out())

# Make predictions and check the accuracy
predictions = clf.predict(X_test)
print(accuracy_score(y_test, predictions))
