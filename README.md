Intraday Volatility Forecasting for Equity and FX
=================================================

I built this project to estimate and forecast intraday volatility for both equities and currency pairs.  
I wanted to show how I handle data, apply microstructure-aware estimators, and test short-horizon models in a way that can be reused in practice.

Project motivation
------------------
I care about short horizon risk because trading decisions often need intraday signals that are robust and quick to compute.  
In my work here, I computed realized volatility at 10-minute, 30-minute, and 1-hour horizons and compared simple linear models with autoregressive baselines.

What I included
---------------
• A Python package under `src/ivf` with functions for realized volatility estimation, model fitting, and plots  
• Two polished notebooks, one on equities and one on FX, that show the workflow end to end  
• A small research note in `docs` that summarizes my results in plain language  
• A demo figure in `assets` so the repo front page has a visual  
• A requirements file to make the setup easy  

Main takeaways
--------------
• For Microsoft, realized volatility is highest at the open, lower mid-day, and picks up again into the close:contentReference[oaicite:0]{index=0}.  
• For QUBT, a micro-cap, the baseline volatility is higher with frequent spikes. OLS fits reasonably in-sample but out-of-sample is unstable:contentReference[oaicite:1]{index=1}.  
• For EUR/JPY and USD/JPY, out-of-sample predictability is more stable with positive R², while EUR/USD remains harder to forecast:contentReference[oaicite:2]{index=2}.  
• Overall, OLS on multi-horizon features outperforms AR(6) benchmarks.

How to run it
-------------
1. Create a fresh Python environment  
2. Install dependencies with `pip install -r requirements.txt`  
3. Open one of the notebooks in the `notebooks` folder  
4. Run all cells to reproduce the plots and model fits  

If you want to dig deeper, the code in `src/ivf` can be imported into any script or notebook. The `docs` folder holds my research note with the main results.

Credits
-------
I developed this project during my time at UC Berkeley and reworked it into a self-contained repo.  
It represents my own research and implementation choices, with a focus on clarity and reusability.
