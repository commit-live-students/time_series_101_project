import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path = 'data/perrin-freres-monthly-champagne.csv'

def q01_load_data(path):
    df = pd.read_csv(path, index_col=False)
    return df
