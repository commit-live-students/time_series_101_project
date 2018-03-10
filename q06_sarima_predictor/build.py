
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace import sarimax
import math
from sklearn.metrics import mean_squared_error
plt.switch_backend('agg')
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model

def q06_sarima_predictor(path):
    tss, tss_valid = q05_sarima_model(path)
    'write your solution here'
    mod = sarimax.SARIMAX(tss['Sales'], order=(5, 1, 1), seasonal_order=(1, 1, 0, 12)).fit()
    plt.figure(figsize=(16, 7))
    plt.plot(tss.index, tss.Sales, color='lightblue')
    plt.plot(tss_valid.index, tss_valid.Sales.values, color='green')

    ## Forecasting
    pred = pd.DataFrame(mod.forecast(len(tss_valid)))
    pred.columns = ['yhat']
    pred.index = tss_valid.index

    ## Converting from log to normal value
    # pred['yhat'] = pred['yhat'].apply(lambda x: int(math.exp(x)-1))

    ## Measuring error.
    measure = math.pow(mean_squared_error(tss_valid.values, pred.values), 0.5)
    return pred, measure

