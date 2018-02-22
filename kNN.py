import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.preprocessing import Imputer
import numpy as np

df = pd.read_csv("crx.data.training",header = None)
df = df.replace('?', pd.np.NaN)

#print(df[15].value_counts())

#print(df)
#df.plot(x=df[], y='col_name_2', style='o')
#filtered_df = df[df[1].notnull()]

# positive_1_withmissing = df[df[(df[15] == '+')][1]]
# print(positive_1_withmissing)
# positive_1 = positive_1_withmissing[positive_1_withmissing[1] != '?' ]
# print(positive_1)

# imp = Imputer(missing_values="NaN", strategy='mean', axis=0)
# df = imp.fit_transform(df[1])
# df[1] = df[1].fillna(value = df[1].mean())
# df = df.dropna()
# mean = df[1].mean()
#df[1].fillna(df[1].mean(), inplace=True)
## print((df[np.isnan(df)]))
print(df)