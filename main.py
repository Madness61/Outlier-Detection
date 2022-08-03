from readFile import read_file
from IQR-Method import IQ
from Boxplot import boxplot
import numpy as np

df = read_file()
splitted = np.array_split(df, 100)


#print(df)
#boxplot(df, 'z')

# IQR: 642 von 10000
# ISO-F: ~1334 von 10000

IQR_Method(df)
