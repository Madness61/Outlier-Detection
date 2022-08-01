import pandas as pd

lst = []
# Gets all coordinates from file and writes it in lst as Martix.
with open(r"C:/Users/manue/OneDrive/Desktop/BA/raw1.xyz") as file:
    count = 0
    for line in file:
        # Can delete, to look at full dataset.
        if count >= 100000:
            break

        # Splits every coordinate in each line and cast float.
        xyz = [float(x) for x in line.split("\t")]
        lst.append(xyz)
        count = count + 1
file.close()

df = pd.DataFrame(data=lst, columns=['x', 'y', 'z'])