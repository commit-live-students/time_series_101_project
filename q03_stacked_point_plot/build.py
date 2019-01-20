# %load q03_stacked_point_plot/build.py
import pandas as pd
import numpy as np
import sys
import datetime
sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns
path = 'data/perrin-freres-monthly-champagne.csv'

def q03_stacked_point_plot(path, 
                           x_column_name='month', 
                           y_column_name='Sales', 
                           hue='year', 
                           order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']):
    df = pd.read_csv(path)
    df = df.rename(columns={'Month': 'month'})
    df.month = pd.to_datetime(df.month)
    df.set_index(x_column_name, inplace=True)
    plt.figure(figsize=(20, 10))
    sns.pointplot(x=df.index.strftime('%b'), y=df['Sales'], hue=df.index.year, x_order=order_of_the_axis, fontsize=20)
    plt.show();



