Intraday volatility findings at a glance
========================================

This note distills the equity and FX results that appear in your original work. Charts on page 1 show the classic U shape intraday pattern for Microsoft with high volatility near the open, a calm mid day area, and a pickup near the close. The table on page 2 reports an OLS fit with R two near zero point eight six in sample and a much weaker out of sample result, and an AR with six lags with in sample R two near zero point six five. fileciteturn0file0

Charts on page 3 show the small cap QUBT with higher baseline volatility and more spikes. The OLS has in sample R two near zero point seven two and out of sample R two near zero point zero six below zero, while the AR with six lags is weaker and turns strongly negative out of sample. fileciteturn0file0

For FX, charts on pages 4 through 6 show EUR USD, EUR JPY, and USD JPY intraday realized volatility at the same three horizons. The note reports that OLS out of sample R two is positive for EUR JPY and for USD JPY around zero point four four, while EUR USD is slightly below zero around zero point zero five. AR with six lags underperforms in each case. fileciteturn0file0

Takeaways for trading
• Simple multi horizon features help at very short horizons, yet a naive AR on a single horizon often loses out of sample
• De seasonalization by time of day and mild regularization would likely improve stability
• Microstructure aware estimators reduce bias when you sample faster than one min
