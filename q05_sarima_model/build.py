
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# import sys
# sys.path.append('./')
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter


def q05_sarima_model(path):
    train, validation = q02_data_splitter(path)
    'write your solution here'
    tss = pd.DataFrame(train['Sales'])
    tss.column = ['Sales']
    tss.index = train['Month'].values

    tss_valid = pd.DataFrame(validation['Sales'])
    tss_valid.column = ['Sales']
    tss_valid.index = validation['Month'].values
    return tss, tss_valid
    

