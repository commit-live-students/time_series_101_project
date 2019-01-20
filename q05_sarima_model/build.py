# %load q05_sarima_model/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# import sys
# sys.path.append('./')
import seaborn as sns
import matplotlib.pyplot as plt
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter

path = 'data/perrin-freres-monthly-champagne.csv'
train, validation = q02_data_splitter(path)

def q05_sarima_model(path):
    tss, tss_valid = train.copy(), validation.copy()
    tss.set_index('Month', inplace=True)
    tss_valid.set_index('Month', inplace=True)
    del tss.index.name, tss_valid.index.name
    return tss, tss_valid



