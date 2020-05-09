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
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model
path = 'data/perrin-freres-monthly-champagne.csv'
tss, tss_valid = q05_sarima_model(path)

def q06_sarima_predictor(path):
    mod = sarimax.SARIMAX(tss['Sales'], order=(5, 1, 1), seasonal_order=(1, 1, 0, 12)).fit()
    plt.figure(figsize=(16, 7))
    plt.plot(tss.index, tss.Sales, color='lightblue')
    plt.plot(tss_valid.index, tss_valid.Sales.values, color='green')

    ## Forecasting

    pred = pd.DataFrame(mod.forecast(len(tss_valid)))
    pred.columns = ['yhat']
    pred.index = tss_valid.index

    measure = math.pow(mean_squared_error(tss_valid.values, pred.values), 0.5)

    return pred, measure

# q06_sarima_predictor(path)
    



