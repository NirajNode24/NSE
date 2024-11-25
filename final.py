import yfinance as yf
import pandas as pd
import os

# Define file path
absolute_path = os.path.abspath('52_week_high_stocks_2024-11-25_17-23-14.csv')

# Read CSV
df = pd.read_csv(absolute_path)
Sname = df["Name"]  # Assuming 'Name' column contains stock symbols

# Initialize result DataFrame
result_df = pd.DataFrame()

# Fetch data for NSE and BSE
for symbol in Sname:
    pass
#       try:
        # Fetch historical data for the stock
#         stock = yf.Ticker(symbol)
#         historical_data = stock.history(period="1y")  # Last 1 year
#         close_data = historical_data['Close']  # Select only the 'Close' column

#         # Take every 25th day of data
#         close_data_25_days = close_data[::25]

#         # Create a temporary DataFrame for the stock
#         stock_df = pd.DataFrame(close_data_25_days)
#         stock_df.columns = [symbol]  # Use stock symbol as column name

#         # Concatenate with result DataFrame
#         result_df = pd.concat([result_df, stock_df], axis=1)
#     except Exception as e:
#         print(f"Error fetching data for {symbol}: {e}")

# # Add shifted columns for DMA (Days Moving Average) calculation
# for i in range(9, -1, -1):
#     result_df[f'DAYS_{i * 25}'] = result_df.iloc[:, 0].shift(-i)

# # Save to CSV
# output_file = 'stock_dma.csv'
# result_df.to_csv(output_file, index=True)

# print(f"The CSV file '{output_file}' has been created successfully.")
