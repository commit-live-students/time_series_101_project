# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/perrin-freres-monthly-champagne.csv'
def q01_load_data(path):
    df = pd.read_csv(path)
    return df.reset_index(drop=True)
   


q01_load_data(path).shape
df = pd.read_csv(path,index_col=False,)
df.drop(df.index,inplace=True)
df.head()
df.shape
df = pd.read_csv(path,index_col=None)
df.head()
df.iloc[:,0]


