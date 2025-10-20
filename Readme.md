# Flask ARIMA / SARIMAX Forecast App

Simple Flask web app to fetch historical stock prices and produce ARIMA / SARIMAX forecasts with plots and HTML tables.

Features
- Interactive web forms to configure ARIMA and SARIMAX parameters.
- Fetches historical price data via yfinance.
- Fits models using statsmodels and returns forecasted prices and plots.
- Saves plots to the static folder for display.

Requirements
- Python 3.8+
- See [requirements.txt](requirements.txt) for required Python packages:
  - yfinance, statsmodels, pandas, numpy, matplotlib, flask

Install
1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```sh
   pip install -r requirements.txt

Run
```sh
   python app.py

