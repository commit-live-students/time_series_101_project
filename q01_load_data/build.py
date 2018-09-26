# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

'write your solution here'
   
def q01_load_data(path):
    df = pd.read_csv(path)
    return df


