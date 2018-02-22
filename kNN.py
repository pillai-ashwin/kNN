import pandas as pd
import numpy as np

df = pd.read_csv("crx.data.training",header = None)
df = df.replace('?', pd.np.NaN)

''' Changing data type of numeric columns to float '''
df[[1,2,7,10,13,14]] = df[[1,2,7,10,13,14]].astype(float)

''' Looping over all columns and handle the missing values '''
for i in range(len(df.columns)):
    if (df[i].dtype == float):
        df[i] = df[i].fillna(np.nanmean(df[i].where(df[15]=="-")))
        df[i] = df[i].fillna(np.nanmean(df[i].where(df[15] == "+")))
    if(df[i].dtype == object):
        df[i] = df[i].fillna(df[i].mode()[0])
df.to_csv(r'crx.training.processed', header=None, index=None, sep=',', mode='w')