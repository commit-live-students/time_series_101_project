# %load q06_sarima_predictor/build.py
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
path='data/perrin-freres-monthly-champagne.csv'
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model
tss, tss_valid = q05_sarima_model(path)

'write your solution here'
def q06_sarima_predictor(path):
    tss, tss_valid = q05_sarima_model(path)
    mod = sarimax.SARIMAX(tss.Sales, trend='n', order=(1,1,1), seasonal_order=(1,1,1,12))
    results = mod.fit(disp=-1)
    
    ## Forecasting 
    pred = pd.DataFrame(results.forecast(len(tss_valid)))
    pred.index = tss_valid.index


    ## Measuring error. 
    measure = math.pow(mean_squared_error(tss_valid.values, pred.values), 0.5)
    return pred,measure



