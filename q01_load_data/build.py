
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def q01_load_data(path):
    'write your solution here'
    data = pd.read_csv(path, encoding='utf-8')
    return data

