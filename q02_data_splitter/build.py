# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data

path = 'data/perrin-freres-monthly-champagne.csv'

'''Write your solution here'''
def q02_data_splitter(data):
    df_1 = pd.read_csv(data)
    df_1['Month'] = pd.to_datetime(df_1['Month'], format = '%Y-%m-%d')
    
    # Assigning the date to split the Datetime 
    split_date = pd.datetime(1971,10,1)
    
    # Split the data, such thatdata less then specific time and other greater then
    df_training = df_1.loc[df_1['Month'] < split_date]
    Valid_test = df_1.loc[df_1['Month'] >= split_date]
    return df_training, Valid_test
    
q02_data_splitter(path)
df = pd.read_csv(path)
df.head()


