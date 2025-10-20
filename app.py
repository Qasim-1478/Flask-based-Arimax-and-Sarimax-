from flask import Flask, jsonify, request, render_template

import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for non-GUI environments


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ARIMA', methods=['POST', 'GET'])
def arima_model():
    if request.method == 'POST':
        # Get form data
        stock_symbol = request.form['stock_symbol']
        days = int(request.form['days'])
        p = int(request.form['p'])
        d = int(request.form['d'])
        q = int(request.form['q'])

        # Fetch historical stock data
        end_date = date.today()
        start_date = end_date - timedelta(days=365*5)  # Last 5 years
        data = yf.download(stock_symbol, start=start_date, end=end_date)

        if data.empty:
            return render_template('ARIMA.html', error="Invalid stock symbol or no data available.")

        # Prepare the data
        ts_data = data['Close'].dropna()

        # Fit ARIMA model
        try:
            model = ARIMA(ts_data, order=(p, d, q))
            model_fit = model.fit()
        except Exception as e:
            return render_template('ARIMA.html', error=f"Error fitting ARIMA model: {e}")

        # Forecast future prices
        forecast = model_fit.forecast(steps=days)
        last_date = ts_data.index[-1]
        forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=days,freq='B')

        forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecasted Close': forecast})
        #forecast_df.set_index('Date', inplace=True)

        #Create and save plot
        plt.figure(figsize=(10,5))
        plt.plot(ts_data.tail(60).index, ts_data.tail(60), label='Historical Close Prices')
        plt.plot(forecast_df['Date'], forecast_df['Forecasted Close'], label='Forecasted Prices', color='red')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'ARIMA Forecast for {stock_symbol}')
        plt.legend()
        plt.grid()
        plot_path = 'static/arimax_output.png'
        plt.savefig(plot_path)
        plt.close()




        return render_template('ARIMA.html', plot_url=plot_path, tables=[forecast_df.to_html(classes='table table-striped table-bordered table-hover text-center',index=False,header=False)], titles=['Forecasted Stock Prices'],zip=zip)
    

    return render_template('ARIMA.html')

@app.route('/SARIMAX', methods=['POST', 'GET'])
def sarimax_model():
    if request.method == 'POST':
        # Get form data
        stock_symbol = request.form['stock_symbol']
        days = int(request.form['days'])
        p = int(request.form['p'])
        d = int(request.form['d'])
        q = int(request.form['q'])
        P = int(request.form['P'])
        D = int(request.form['D'])
        Q = int(request.form['Q'])
        s = int(request.form['s'])

        # Fetch historical stock data
        end_date = date.today()
        start_date = end_date - timedelta(days=365*5)  # Last 5 years
        data = yf.download(stock_symbol, start=start_date, end=end_date)

        if data.empty:
            return render_template('SARIMAX.html', error="Invalid stock symbol or no data available.")

        # Prepare the data
        ts_data = data['Close'].dropna()

        # Fit SARIMAX model
        try:
            model = SARIMAX(ts_data, order=(p, d, q), seasonal_order=(P, D, Q, s))
            model_fit = model.fit(disp=False)
        except Exception as e:
            return render_template('SARIMAX.html', error=f"Error fitting SARIMAX model: {e}")

        # Forecast future prices
        forecast = model_fit.forecast(steps=days)
        last_date = ts_data.index[-1]
        forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=days,freq='B')

        forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecasted Close': forecast})
        #forecast_df.set_index('Date', inplace=True)

        #Create and save plot
        plt.figure(figsize=(10,5))
        plt.plot(ts_data.tail(60).index, ts_data.tail(60), label='Historical Close Prices')
        plt.plot(forecast_df['Date'], forecast_df['Forecasted Close'], label='Forecasted Prices', color='red')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'SARIMAX Forecast for {stock_symbol}')
        plt.legend()
        plt.grid()
        plot_path = 'static/sarimax_output.png'
        plt.savefig(plot_path)
        plt.close()




        return render_template('SARIMAX.html', plot_url=plot_path, tables=[forecast_df.to_html(classes='table table-striped table-bordered table-hover text-center',index=False,header=False)], titles=['Forecasted Stock Prices'],zip=zip)
    return render_template('SARIMAX.html')
    

@app.route('/ABOUT_ME')
def about_me():
    return render_template('ABOUT_ME.html')




if __name__ == '__main__':
    app.run(debug=True)