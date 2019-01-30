# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data

'''Write your solution here'''
def q02_data_splitter(path):
    
    df = q01_load_data(path)
    df['Month'] =  pd.to_datetime(df['Month'])
    X_train = df[df['Month'] < datetime.datetime(1971,10,1,0)]
    X_valid = df[df['Month'] >=datetime.datetime(1971,10,1)]  
    
    return X_train, X_valid
path = 'data/perrin-freres-monthly-champagne.csv'
q02_data_splitter(path)


