import numpy as np
import pandas as pd

def realized_volatility(prices, resample_rule="1T", bucket_minutes=10):
    """
    Compute realized volatility by summing squared returns within a bucket.
    prices: pandas Series of prices indexed by time
    resample_rule: target sampling like 1T for one min
    bucket_minutes: window length in minutes
    """
    if not isinstance(prices, pd.Series):
        raise TypeError("prices must be a pandas Series")
    px = prices.dropna().sort_index().astype(float).resample(resample_rule).last().dropna()
    logp = np.log(px.values)
    r = np.diff(logp)
    rv1 = pd.Series(r ** 2, index=px.index[1:])
    rv_bucket = rv1.rolling(window=bucket_minutes).sum().dropna()
    return rv_bucket

def multi_horizon_features(prices, resample_rule="1T"):
    """
    Build a DataFrame with realized volatility at ten, thirty, and sixty min.
    """
    rv10 = realized_volatility(prices, resample_rule=resample_rule, bucket_minutes=10)
    rv30 = realized_volatility(prices, resample_rule=resample_rule, bucket_minutes=30)
    rv60 = realized_volatility(prices, resample_rule=resample_rule, bucket_minutes=60)
    df = pd.concat([rv10.rename("rv_10m"), rv30.rename("rv_30m"), rv60.rename("rv_60m")], axis=1).dropna()
    # align so that features predict the next step of the ten min rv
    y = df["rv_10m"].shift(-1)
    X = df[["rv_10m", "rv_30m", "rv_60m"]]
    # avoid negative shift literal in code by reindex trick
    y = y.iloc[:-1]
    X = X.iloc[:-1]
    return X, y
