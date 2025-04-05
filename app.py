import streamlit as st
import yfinance as yf
import os
import pandas as pd

# Title
st.title("Candle Research: Download Stock Data")

# Text input for tickers
ticker_input = st.text_input("Enter tickers (space-separated, e.g., SPY AAPL NVDA TSLA):", "SPY AAPL NVDA TSLA")
tickers = ticker_input.split() # Split input into list

# Date range (hard core for now)
start_date = "2020-01-01"
end_date = "2025-04-05"

# Button to download
if st.button("Download Data"):
    # Create data folder
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Download and save data
    for ticker in tickers:
        with st.spinner(f"Downloading data for {ticker}..."):
            data = yf.download(ticker, start=start_date, end=end_date, interval="1d", auto_adjust=False)
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)
            data.to_csv(f"data/{ticker}.csv")
        st.success(f"Saved {ticker} data to data/{ticker}.csv")