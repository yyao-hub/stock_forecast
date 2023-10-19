"""
File: StockPriceForecast.py
Author: Yuanbin Yao
Date: 10/19/2023
Description: Get stock price forecast from money.cnn.com by inputting a ticker
"""

import requests
import re


def get_stock_forecast(ticker):
    # Get the URL for the specified ticker
    url = f"https://money.cnn.com/quote/forecast/forecast.html?symb={ticker}"

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    # Use regular expressions to extract four prices from response
    content = r.text
    current_price = re.search(r'last price of (\d+\.\d+)', content)
    high_estimate = re.search(r'high estimate of (\d+\.\d+)', content)
    medium_estimate = re.search(r'median target of (\d+\.\d+)', content)
    low_estimate = re.search(r'low estimate of (\d+\.\d+)', content)

    # Get the four stock prices if all present in the response, return None otherwise
    if current_price and high_estimate and medium_estimate and low_estimate:
        return (
            float(current_price.group(1)),
            float(high_estimate.group(1)),
            float(medium_estimate.group(1)),
            float(low_estimate.group(1))
        )
    else:
        return None


# Usage Example
if __name__ == '__main__':

    symbol = "AAPL"
    forecast_data = get_stock_forecast(symbol)
    if forecast_data:
        print(f"Stock Forecast for {symbol}:")
        print(f"Current Price: {forecast_data[0]}")
        print(f"High Estimate: {forecast_data[1]}")
        print(f"Medium Estimate: {forecast_data[2]}")
        print(f"Low Estimate: {forecast_data[3]}")
