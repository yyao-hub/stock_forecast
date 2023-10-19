"""
File: StockPriceForecastTest.py
Author: Yuanbin Yao
Date: 10/19/2023
Description: unit tests for getting stock price forecast
"""

import unittest
from get_stock_forecast import get_stock_forecast


class TestStockForecast(unittest.TestCase):
    def test_get_stock_forecast(self):
        # Test for a given ticker. For example, AAPL
        ticker = "AAPL"
        forecast_data = get_stock_forecast(ticker)
        self.assertIsNotNone(forecast_data)
        self.assertEqual(len(forecast_data), 4)
        self.assertIsInstance(forecast_data[0], float)
        self.assertIsInstance(forecast_data[1], float)
        self.assertIsInstance(forecast_data[2], float)
        self.assertIsInstance(forecast_data[3], float)


if __name__ == '__main__':
    unittest.main()
