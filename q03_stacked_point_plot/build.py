
import pandas as pd
import numpy as np
plt.switch_backend('agg')
#import sys
#sys.path.append('./')
from sklearn.model_selection import train_test_split
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
import seaborn as sns

def q03_stacked_point_plot(path, x_column_name='month', y_column_name='Sales', hue='year',
        order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']):
    train, validation = q02_data_splitter(path)
    #'write your solution here'
    ts = pd.DataFrame(train)
    ts['year'] = ts['Month'].dt.year
    ts['month'] = ts['Month'].dt.strftime('%b')
    return sns.pointplot(x=x_column_name, y=y_column_name, hue=hue, data=ts, x_order=order_of_the_axis)

