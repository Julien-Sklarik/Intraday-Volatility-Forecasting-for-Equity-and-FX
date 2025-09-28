import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AutoReg

def fit_ols(X, y):
    X1 = sm.add_constant(X)
    model = sm.OLS(y, X1, missing='drop')
    res = model.fit()
    return res

def fit_ar6(y):
    model = AutoReg(y, lags=6, old_names=False)
    res = model.fit()
    return res

def r2_score(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
