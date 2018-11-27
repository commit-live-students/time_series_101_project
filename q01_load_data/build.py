import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/perrin-freres-monthly-champagne.csv'

"write your solution here"
def q01_load_data(data):

    df = pd.read_csv(data)
    #df = df.drop()
    return df
q01_load_data(path)
