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

def q04_boxplot(path, x="month", y="Sales", kind="box", order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
       'Sep', 'Oct', 'Nov', 'Dec'], size=8):
    train, validation = q02_data_splitter(path)
    "write your solution here"
    

