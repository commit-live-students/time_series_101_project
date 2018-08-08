# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data

#'''Write your solution here''

def q02_data_splitter(path):
    tss=q01_load_data(path)
    tss['Month']=pd.to_datetime(tss['Month'])
    X_train = tss[tss['Month'] <datetime.datetime(1971, 10, 1, 0, 0, 0)]
    X_valid = tss[tss['Month'] >=datetime.datetime(1971, 10, 1, 0, 0, 0)]
    return X_train, X_valid




