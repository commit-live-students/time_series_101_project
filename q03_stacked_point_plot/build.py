# %load q03_stacked_point_plot/build.py
import pandas as pd
import numpy as np
#import sys
#sys.path.append('./')
from sklearn.model_selection import train_test_split
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns

#'write your solution here'
    
def q03_stacked_point_plot(path,x_column_name='month',y_column_name='Sales',hue='year',order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']):
    x_train,x_valid = q02_data_splitter(path)
    #x_train['Month'] = pd.to_datetime(df['Month'])
    x_train['year']  = x_train['Month'].dt.year
    x_train['month'] = x_train['Month'].dt.strftime('%b')
    plt.figure(figsize=(16, 7))
    sns.pointplot(x='month', y='Sales', hue='year', data=x_train, x_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
       'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel('month')
    plt.ylabel('$ millions')
    plt.title('Sales')
    plt.legend(loc='upper right')
    

