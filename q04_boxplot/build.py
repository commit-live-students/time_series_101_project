# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import datetime
import sys
sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter

path = 'data/perrin-freres-monthly-champagne.csv'

def q04_boxplot(path, 
                x='month', 
                y='Sales', 
                kind='box',
                order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'],
                height=8):
    x_train,_ = q02_data_splitter(path)
    x_train = x_train.rename(columns={'Month': 'month'})
    x_train.set_index(x, inplace=True)
    plt.figure(figsize=(20, 10))
    sns.factorplot(x=x_train.index.month, y='Sales', kind=kind, data=x_train, aspect=float(16/7))
    plt.xlabel('month', fontsize=20)
    plt.ylabel('Sales', fontsize=20)
    plt.show();




