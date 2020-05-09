# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data

path = 'data/perrin-freres-monthly-champagne.csv'

# '''Write your solution here'''

def q02_data_splitter(path):
    df = q01_load_data(path)
    df['Month'] = pd.to_datetime(df['Month'])
    split_date = pd.datetime(1971,10,1)
    X_train = df[df['Month'] < split_date]
    X_valid = df[df['Month'] >=split_date]
    return X_train,X_valid



