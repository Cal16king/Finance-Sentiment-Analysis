import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import datetime
import numpy as np

# Define the stock ticker and the start/end dates
ticker = "F"
end_date_str = '2024-04-19'
end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
start_date = end_date - relativedelta(days=18)

# Get stock price history
stock = yf.Ticker(ticker)
stock_hist = stock.history(start=start_date, end=end_date)

# Get closing prices with dates
stock_day_closes = pd.DataFrame(stock_hist, columns=["Close"])

# Create training data with dates as x-axis
x_train = np.array(pd.to_datetime(stock_day_closes.index))
y_train = stock_day_closes["Close"].to_numpy()

# Plot the data points with dates on the x-axis
plt.plot(x_train, y_train, label="Stock Price")
plt.title("F, Closing Prices")
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation=45)  # Rotate x-axis ticks for better readability

# Show the legend and the plot
plt.legend()
plt.show()
