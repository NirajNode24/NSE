import yfinance as yf
import pandas as pd

# Fetch data for NSE and BSE
symbols = {
    "SKYGOLD": "SKYGOLD.NS",  # NSE symbol
    "541967": "541967.BO"     # BSE symbol
}

# Create a DataFrame to store results
result_df = pd.DataFrame()

for name, symbol in symbols.items():
    try:
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period="1y")  # Last 1 year
        historical_data = historical_data.sort_index(ascending=False)  # Sort in descending order
        close_data = historical_data['Close']  # Select only the 'Close' column
        
        # Select data at intervals of 25 days
        close_data_25_days = close_data[::25]
        
        # Prepare DAYS columns
        days_dict = {
            f'DAYS_{i*25}': [close_data_25_days.iloc[i]]
            if i < len(close_data_25_days) else [None]
            for i in range(len(close_data_25_days))
        }
        
        # Create a DataFrame for the stock
        stock_df = pd.DataFrame(days_dict)
        stock_df.insert(0, 'Name', name)
        
        # Append to result DataFrame
        result_df = pd.concat([result_df, stock_df], ignore_index=True)
    except Exception as e:
        print(f"Error fetching data for {name} ({symbol}): {e}")

# Save to CSV
result_df.to_csv('formatted_stock_dma.csv', index=False)

print("The CSV file 'formatted_stock_dma.csv' has been created successfully.")
