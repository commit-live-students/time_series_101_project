# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
import datetime
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter

def q04_boxplot(path, x='month', y='Sales', kind='box', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
       'Sep', 'Oct', 'Nov', 'Dec'], size=8):
    train, validation = q02_data_splitter(path)
    sns.factorplot(data=train,x=x, y=y, kind=kind, order=order, size=size)
    plt.xlabel('month')
    plt.ylable('Sales')
    plt.show()
 
    


import seaborn as sns
import matplotlib.pyplot as plt

sns.factorplot(data= train, x='Month', y='Sales', kind='box', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
       'Sep', 'Oct', 'Nov', 'Dec'], size=8)


