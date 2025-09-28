Intraday Volatility Forecasting for Equity and FX
=================================================

I built this project to estimate and forecast intraday volatility for both stocks and currency pairs. 
My goal was to turn raw high-frequency data into stable realized volatility measures and test 
whether short-horizon forecasts can be extracted in a simple and transparent way.

Why I worked on this
--------------------
I wanted to better understand how intraday risk evolves within a trading session. 
I focused on realized volatility at ten minute, thirty minute, and one hour horizons. 
I then compared a simple regression on multi-horizon inputs with an autoregressive benchmark.

What I did
----------
• I computed realized volatility measures from one minute returns, using both direct sums and bias-reduced estimators.  
• I fitted OLS models with multiple horizon inputs, similar to a HAR approach, and compared them to AR models with six lags.  
• I tested both equities (large cap and small cap) and major FX pairs.  
• I documented the whole process in notebooks and summarized results in a compact research note.  

Main insights
-------------
• Volatility is highest at the market open, decays mid-day, and rises again near the close.  
• OLS models perform well in sample but often lose predictive power out of sample, especially without de-seasonalizing by time of day.  
• In FX, I found that EURJPY and USDJPY had stable positive out of sample R², while EURUSD did not.  
• Small cap names showed much higher volatility clustering compared to large caps.  

Preview
-------
![Demo intraday RV shape](assets/figures/rv_demo.png)

Project structure
-----------------
• src  Python package with functions for realized volatility, model fitting, and plots  
• notebooks  Two polished notebooks that cover equity and FX analysis  
• docs  A short research note with the main results I got  
• assets  A demo figure for quick visualization on the front page  
• data  Folder to place input CSVs if not pulled via API  
• results  Saved tables and plots  

How to run my work
------------------
1. Create a new virtual environment  
2. Install dependencies with `pip install -r requirements.txt`  
3. Open any notebook in the notebooks folder and run it end to end  
4. The docs folder contains my research summary in plain text  

Why this matters
----------------
My work shows that realized volatility features can capture short horizon risk patterns and provide 
useful signals, even if forecasts remain fragile at very high frequency. 
This type of analysis can help build intuition for both execution strategies and short horizon risk management.

Credit
------
This project started from work I did during my time at UC Berkeley MFE. 
I restructured it into a standalone project with reusable code, so I can use it as a base for further research 
and as a demonstration of my approach to intraday data and volatility forecasting.
