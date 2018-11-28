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

path = 'data/perrin-freres-monthly-champagne.csv'
x_column_name='month'
y_column_name='Sales'
hue='year'
order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']


def q03_stacked_point_plot(path,x_column_name='month',y_column_name='Sales',hue='year',order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']):
    X_train,X_valid = q02_data_splitter(path)
    X_train['year']  = X_train['Month'].dt.year
    X_train['month'] = X_train['Month'].dt.strftime('%b')
    plt.figure(figsize=(16, 7))
    sns.pointplot(x=x_column_name, y=y_column_name, hue=hue, data=X_train, x_order=order_of_the_axis)
    plt.xlabel('month')
    plt.ylabel('sales')
    plt.legend(title='year',loc='upper left')
    plt.show()

# q03_stacked_point_plot(path,x_column_name,y_column_name,hue,order_of_the_axis)


