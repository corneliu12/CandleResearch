import yfinance as yf
import os
import pandas as pd

# Define tickers and date range
tickers = ["SPY", "AAPL", "NVDA", "TSLA"]
start_date = "2020-04-05"
end_date = "2025-04-05"

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Download and save data for each ticker
for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date, interval="1d", auto_adjust=False)
    # Remove the "Ticker" level from column names (if present)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    # Save to CSV
    data.to_csv(f"data/{ticker}_data.csv")
    print(f"Saved {ticker} data to data/{ticker}_data.csv")