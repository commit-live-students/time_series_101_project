# %load q06_sarima_predictor/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace import sarimax
import math
from sklearn.metrics import mean_squared_error
#import sys
#sys.path.append('./')
from greyatomlib.time_series_101_project.q05_sarima_model.build import q05_sarima_model
plt.switch_backend('agg')
path = 'data/perrin-freres-monthly-champagne.csv'

'write your solution here'
def q06_sarima_predictor(path):
    tss, tss_valid = q05_sarima_model(path)

    # Model
    model = sarimax.SARIMAX(tss['Sales'],trend='n',order=(1,1,1),seasonal_order=(1,1,1,12))
    results = model.fit(disp=-1)

    # Forecasting
    y_pred = pd.DataFrame(results.forecast(len(tss_valid)))
    y_pred.index=tss_valid.index

    # Evaluation metric-rmse
    rmse = math.pow(mean_squared_error(tss_valid.values,y_pred.values),0.5)

    return y_pred,rmse


