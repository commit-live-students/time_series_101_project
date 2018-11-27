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
    X_train,_ = q02_data_splitter(path)

    X_train['Year'] = X_train['Month'].dt.year
    X_train['month'] = X_train['Month'].dt.strftime('%b')

    plt.figure(figsize=(16,4))
    sns.pointplot('month','Sales',hue='Year',data=X_train,order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
           'Sep', 'Oct', 'Nov', 'Dec'])
    plt.ylabel('Sales')
    plt.xlabel('month')
    plt.legend(loc='upper left')
    plt.show()


