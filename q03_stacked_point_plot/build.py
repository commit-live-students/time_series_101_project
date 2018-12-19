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


path = 'data/perrin-freres-monthly-champagne.csv'

#'write your solution here'
def q03_stacked_point_plot(path,x,y,hue,x_order):
    df = pd.read_csv(path, index_col=False)
    df["Month"] = pd.to_datetime(df["Month"])
    df["year"] = df["Month"].dt.year
    df["month"] = df["Month"].dt.strftime('%b')
    x = "month"
    y = "Sales"
    hue = "year"
    x_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ## Split the data into train and test
    X_train = df[df["Month"] < "1971-10-01"]
    X_valid = df[df["Month"] >="1971-10-01"]
    data = X_train
    plt.figure(figsize=(16, 7))
    sns.pointplot(x=x, y=y, hue=hue, data=data, x_order=x_order)
    plt.xlabel("Month")
    plt.ylabel("$ millions")
    plt.title("Perrin Freres Monthly Champagne")
    plt.legend(loc='upper right')
