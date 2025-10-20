# Flask ARIMA / SARIMAX Forecast App

Simple Flask web app to fetch historical stock prices and produce ARIMA / SARIMAX forecasts with plots and HTML tables.

Features
- Interactive web forms to configure ARIMA and SARIMAX parameters.
- Fetches historical price data via yfinance.
- Fits models using statsmodels and returns forecasted prices and plots.
- Saves plots to the static folder for display.

Quick links
- App entry: [`app.py`](app.py) — contains the route handlers [`app.home`](app.py), [`app.arima_model`](app.py), [`app.sarimax_model`](app.py) and [`app.about_me`](app.py).
- Templates: [templates/index.html](templates/index.html), [templates/ARIMA.html](templates/ARIMA.html), [templates/SARIMAX.html](templates/SARIMAX.html), [templates/ABOUT_ME.html](templates/ABOUT_ME.html)
- Requirements: [requirements.txt](requirements.txt)
- Static output images: saved to `static/arimax_output.png` and `static/sarimax_output.png`

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