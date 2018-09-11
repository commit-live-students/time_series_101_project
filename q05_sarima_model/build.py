# %load q05_sarima_model/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter


path = 'data/perrin-freres-monthly-champagne.csv'


'write your solution here'
def q05_sarima_model(data):
    
    train, validation = q02_data_splitter(data)
    train = pd.DataFrame(train)
    validation = pd.DataFrame(validation)
    train.index, validation.index = train['Month'], validation['Month']
    train = train.drop('Month', 1)
    validation = validation.drop('Month', 1)
    return (train, validation)

q05_sarima_model(path)


