import yfinance as yf
import pandas as pd
import os

# Input file path
input_file = '52_week_high_stocks_2024-11-26_10-19-55.csv'
output_file = 'formatted_stock_dma.csv'
skipped_symbols_file = 'skipped_symbols.log'

if not os.path.exists(input_file):
    raise FileNotFoundError(f"The input file '{input_file}' does not exist.")

# Read the stock symbols
df = pd.read_csv(input_file)
if 'Name' not in df.columns:
    raise ValueError("The input file does not contain a 'Name' column.")

# Extract unique stock names
Sname = df["Name"].dropna().unique()

# Sanitize stock names and create symbols dictionary
symbols = {}
for symbol in Sname:
    sanitized_symbol = symbol.replace(" ", "-")  # Replace spaces with dashes
    symbols[symbol] = f"{sanitized_symbol}.NS"  # Modify the suffix as per your exchange

# Check if output file exists, create with headers if not
if not os.path.exists(output_file):
    with open(output_file, 'w') as f:
        pd.DataFrame(columns=['Name', 'DAYS_0', 'DAYS_25', 'DAYS_50', 'DAYS_75']).to_csv(f, index=False)

# Process each symbol and append to CSV
for name, symbol in symbols.items():
    try:
        print(f"Processing: {name} ({symbol})")
        stock = yf.Ticker(symbol)

        # Verify if the symbol has valid data
        info = stock.info
        if 'regularMarketPrice' not in info or info['regularMarketPrice'] is None:
            print(f"Symbol {symbol} appears invalid or delisted. Logging and skipping...")
            with open(skipped_symbols_file, 'a') as log_file:
                log_file.write(f"{name} ({symbol}) - Invalid or delisted\n")
            continue

        historical_data = stock.history(period="1y")  # Last 1 year
        if historical_data.empty:
            print(f"No data available for {symbol}. Logging and skipping...")
            with open(skipped_symbols_file, 'a') as log_file:
                log_file.write(f"{name} ({symbol}) - No historical data\n")
            continue

        historical_data = historical_data.sort_index(ascending=False)  # Sort in descending order
        close_data = historical_data['Close']  # Select only the 'Close' column

        # Select data at intervals of 25 days
        close_data_25_days = close_data[::25]

        # Prepare DAYS columns
        days_dict = {
            f'DAYS_{i*25}': [close_data_25_days.iloc[i]] if i < len(close_data_25_days) else [None]
            for i in range(len(close_data_25_days))
        }

        # Create a DataFrame for the stock
        stock_df = pd.DataFrame(days_dict)
        stock_df.insert(0, 'Name', name)

        # Append to the output CSV file
        with open(output_file, 'a') as f:
            stock_df.to_csv(f, header=False, index=False)
    except Exception as e:
        print(f"Error fetching data for {name} ({symbol}): {e}")
        with open(skipped_symbols_file, 'a') as log_file:
            log_file.write(f"{name} ({symbol}) - {e}\n")

print(f"The CSV file '{output_file}' has been updated successfully.")
print(f"Skipped symbols have been logged to '{skipped_symbols_file}'.")



# from playwright.sync_api import sync_playwright, TimeoutError

# base_url = "https://www.screener.in"
# company_base_url = "https://www.screener.in/company/"
# Names = []
# Final = []

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     url = "https://www.screener.in/screens/2232034/52-week-high-by-irshad/?sort=name&limit=25&order=asc"
#     page.goto(url)
#     all_links = []
#     while True:
#         page.wait_for_selector("body > main > div.card.card-large > div.responsive-holder.fill-card-width > table > tbody > tr")
#         rows = page.query_selector_all("body > main > div.card.card-large > div.responsive-holder.fill-card-width > table > tbody > tr")
#         for row in rows:
#             link_element = row.query_selector("td:nth-child(2) > a")
#             if link_element:
#                 relative_url = link_element.get_attribute("href")
#                 full_link = base_url + relative_url
#                 all_links.append(full_link)
#         try:
#             next_button = page.get_by_role("link", name="Next ")
#             if not next_button.is_visible():
#                 break
#             next_button.click()
#             page.wait_for_load_state("networkidle")
#         except TimeoutError:
#             break

#     browser.close()

# # Cleaning up the extracted URLs
# for link in all_links:
#     if link.startswith(company_base_url):
#         cleaned_url = link[len(company_base_url):]
#         if cleaned_url.endswith("/consolidated/"):
#             cleaned_url = cleaned_url[:-len("/consolidated/")]
#         elif cleaned_url.endswith("/"):
#             cleaned_url = cleaned_url[:-1] 
#         Names.append(cleaned_url)

# # Print cleaned links
# for cleaned_url in Names:
#     if cleaned_url.isalpha():
#         result = "".join([cleaned_url,".NS"])
#         Final.append(result)
#     elif cleaned_url.isnumeric():
#         result = "".join([cleaned_url,".BSE"])
#         Final.append(result)

