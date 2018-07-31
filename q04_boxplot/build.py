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

'write your solution here'
def q04_boxplot(path,x='month',y='Sales',kind='box',order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'],size=8):
    
    x_train,x_valid = q02_data_splitter(path)
    x_train['month'] = x_train['Month'].dt.strftime('%b')
    x_train['year'] = x_train['Month'].dt.year
    plt.figure(figsize=(16,7))
    sns.factorplot(x= x,y=y,data=x_train,kind=kind,order=order,size=size)
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Sales in Millions')


