# %load q05_sarima_model/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
path = 'data/perrin-freres-monthly-champagne.csv'
train, validation = q02_data_splitter(path)


'write your solution here'
def q05_sarima_model(path):
    train.index = train['Month']
    train.drop(labels=['Month'],axis=1,inplace=True)
    validation.index = validation['Month']
    validation.drop(labels=['Month'],axis=1,inplace=True)
    return train,validation



