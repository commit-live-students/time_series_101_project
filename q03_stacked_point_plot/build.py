import pandas as pd
import numpy as np
#import sys
#sys.path.append('./')
from sklearn.model_selection import train_test_split
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import seaborn as sns

def q03_stacked_point_plot(path, x_column_name="month", y_column_name="Sales", hue="year",
        order_of_the_axis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']):
    train, validation = q02_data_splitter(path)
    #"write your solution here"
    
