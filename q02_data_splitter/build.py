# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data

# path = 'data/perrin-freres-monthly-champagne.csv'
def q02_data_splitter(path):
    data = q01_load_data(path)
    data['Month'] = pd.to_datetime(data['Month'])
    data['Month']=[d.date() for d in data['Month']]
    X_train = [d for d in data['Month'] if d < datetime.date(1971, 10, 1)]
    X_train = pd.to_datetime(X_train)
    X_train = pd.DataFrame(X_train)
    X_valid = [d for d in data['Month'] if d >= datetime.date(1971, 10, 1)]
    X_valid = pd.to_datetime(X_valid)
    X_valid = pd.DataFrame(X_valid)
    return X_train,X_valid












type(X_train)





