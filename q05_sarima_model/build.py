# %load q05_sarima_model/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
path='data/perrin-freres-monthly-champagne.csv'
train, validation = q02_data_splitter(path)


'write your solution here'
def q05_sarima_model(path):
    df = pd.read_csv(path)
    df['Month']=pd.to_datetime(df['Month'])
    df = df.set_index('Month')
    tss = df[:93]
    tss_valid = df[93:]
    tss.index.names = [None]
    tss_valid.index.names = [None]
    return tss,tss_valid
q05_sarima_model(path)


