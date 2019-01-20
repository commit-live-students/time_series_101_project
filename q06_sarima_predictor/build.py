# %load q06_sarima_predictor/build.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from statsmodels.tsa.statespace import sarimax
import math
from sklearn.metrics import mean_squared_error
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model
path = 'data/perrin-freres-monthly-champagne.csv'
tss, tss_valid = q05_sarima_model(path)

def q06_sarima_predictor(path):
    model = sarimax.SARIMAX(tss.Sales, trend='n', order=(1,1,1), seasonal_order=(1,1,1,12))
    results_SARIMAX = model.fit(disp=-1)
    pred = pd.DataFrame(results_SARIMAX.forecast(len(tss_valid)))
    pred.columns = ['y_pred']
    pred.index = tss_valid.index
    measure = math.pow(mean_squared_error(tss_valid.values, pred.values), 0.5)
    return pred, measure



