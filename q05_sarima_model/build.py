# %load q05_sarima_model/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# import sys
# sys.path.append('./')
path='data/perrin-freres-monthly-champagne.csv'
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
train, validation = q02_data_splitter(path)
import datetime


'write your solution here'
def q05_sarima_model(path):
    train, validation = q02_data_splitter(path)
    train.index=train['Month']
    train=train[['Sales']]
    train.index.name=None

    validation.index=validation['Month']
    validation=validation[['Sales']]
    validation.index.name=None
    return train, validation
    
    


