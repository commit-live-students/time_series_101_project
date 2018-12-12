# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/perrin-freres-monthly-champagne.csv'

# 'write your solution here'
   
def q01_load_data(path):
    df = pd.read_csv(path)
    df.reset_index(drop=True, inplace=True)
    return df

# q01_load_data(path)




