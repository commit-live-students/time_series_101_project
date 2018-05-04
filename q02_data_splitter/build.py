import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data
path = 'data/perrin-freres-monthly-champagne.csv'

def q02_data_splitter(path):
    data = q01_load_data(path)
    data["Month"] = pd.to_datetime(data["Month"])
    X_train = data[data["Month"] < '1971-10-01']
    X_valid = data[data["Month"] >= '1971-10-01']
    return X_train,X_valid
