Intraday Volatility Forecasting for Equity and FX
=================================================

A compact research style project that estimates and predicts intraday volatility for both stocks and currency pairs.  
It showcases clean data handling, microstructure aware estimators, and short horizon forecasting in a way that reads like a professional project rather than class work.

---

Why this matters
----------------
* Intraday risk moves fast. Firms care about nowcasts and next step forecasts that are stable and reproducible.  
* The code computes realized volatility at 10-minute, 30-minute, and 1-hour horizons and compares simple linear models with autoregressive baselines.  
* The repo carries ready to run notebooks plus a small demo figure for quick visual confirmation.  

---

What you can run
----------------
* Notebooks for equity and FX under the `notebooks` folder  
  They call helper functions to compute realized volatility, fit models, and plot the term structure.  

* A compact research note in the `docs` folder  
  It summarizes results with references to charts and metrics.  

---

Preview
-------
![Demo intraday RV shape](assets/figures/rv_demo.png)

---

High level method
-----------------
* Prices are turned into log returns at 1-minute frequency.  
* Squared returns are summed within 10-minute, 30-minute, and 1-hour buckets to form realized volatility features.  
* Two-scale ideas reduce microstructure bias when sampling at high frequency.  
* Forecasts use an OLS on multi-horizon features and a simple AR with six lags as a control.  
* Evaluation is out of sample using a last-third split.  

---

Main contents
-------------
* `src`  
  Python package `ivf` with utilities for realized volatility, model fitting, and plots  

* `notebooks`  
  Two polished notebooks for equity and FX  

* `docs`  
  A short research note with key findings  

* `assets`  
  A demo figure you can show on the repo front page  

* `data`  
  Place any private CSV data here if you cannot pull from an API  

* `results`  
  Saved figures and tables go here  

---

How to use
----------
1. Create a fresh environment  
2. Install dependencies from `requirements.txt`  
3. Open the notebooks and run end to end  
4. See the `docs` folder for a compact story and numbers you can cite during calls  

---

Credit
------
This work originated during Berkeley MFE study and was reworked into a self-contained project with a professional slant.
