import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from statsmodels.tsa.statespace import sarimax
import math
from sklearn.metrics import mean_squared_error
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model

def q06_sarima_predictor(path):
    tss, tss_valid = q05_sarima_model(path)
    "write your solution here"
    
