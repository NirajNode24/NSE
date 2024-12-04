import pandas as pd
import yfinance as yf
import time  # For introducing delays if needed

# Read the CSV file
df = pd.read_csv('52_week_high_stocks_2024-11-26_10-19-55.csv')

# Extract unique stock names
Sname = df["Name"].dropna().unique()

symbols = {}
for name in Sname:
    clean_name = name.strip()  # Remove unwanted spaces
    if clean_name:  # Ensure the name is not empty after cleaning
        # Construct the symbol dynamically based on the name
        # Assuming ".NS" for NSE; modify as needed
        symbol = f"{clean_name.replace(' ', '')}.NS"
        symbols[clean_name] = symbol

# Fetch data for each symbol
for exchange, symbol in symbols.items():
    try:
        print(f"\nFetching data for {symbol} ({exchange})...\n")
        
        # Initialize the stock
        stock = yf.Ticker(symbol)
        
        # Fetch historical data (last 1 year)
        historical_data = stock.history(period="1y")
        print(f"Historical data for {symbol} ({exchange}):\n", historical_data)
        
        # Fetch stock info
        stock_info = stock.info
        print(f"\nStock info for {symbol} ({exchange}):\n", stock_info)
        
    except Exception as e:
        print(f"Error fetching data for {symbol} ({exchange}): {e}")
        
    # Optional: Add a delay to avoid hitting rate limits
    time.sleep(1)
