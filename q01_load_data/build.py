# %load q01_load_data/build.py
import pandas as pd
import numpy as np

path = 'data/perrin-freres-monthly-champagne.csv'

def q01_load_data(path):
    df = pd.read_csv(path)
    return df



