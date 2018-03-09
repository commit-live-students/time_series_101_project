
import pandas as pd
import numpy as np
import datetime
import math
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data


def q02_data_splitter(path):
    data = q01_load_data(path)	
    data['Month'] = pd.to_datetime(data['Month'])
    x_train = data[data['Month'] < datetime.datetime(1971, 10, 1, 0, 0, 0)]
    x_valid = data[data['Month'] >= datetime.datetime(1971, 10, 1, 0, 0, 0)]
    return x_train, x_valid

