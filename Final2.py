from playwright.sync_api import sync_playwright, TimeoutError
import pandas as pd
import yfinance as yf
from datetime import date
import time

current_date = date.today()



base_url = "https://www.screener.in"
company_base_url = "https://www.screener.in/company/"
Names = []
Final = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    url = "https://www.screener.in/screens/2232034/52-week-high-by-irshad/?sort=name&limit=25&order=asc"
    page.goto(url)
    all_links = []
    while True:
        page.wait_for_selector("body > main > div.card.card-large > div.responsive-holder.fill-card-width > table > tbody > tr")
        rows = page.query_selector_all("body > main > div.card.card-large > div.responsive-holder.fill-card-width > table > tbody > tr")
        for row in rows:
            link_element = row.query_selector("td:nth-child(2) > a")
            if link_element:
                relative_url = link_element.get_attribute("href")
                full_link = base_url + relative_url
                all_links.append(full_link)
        try:
            next_button = page.get_by_role("link", name="Next ")
            if not next_button.is_visible():
                break
            next_button.click()
            page.wait_for_load_state("networkidle")
        except TimeoutError:
            break

    browser.close()

for link in all_links:
    if link.startswith(company_base_url):
        cleaned_url = link[len(company_base_url):]
        if cleaned_url.endswith("/consolidated/"):
            cleaned_url = cleaned_url[:-len("/consolidated/")]
        elif cleaned_url.endswith("/"):
            cleaned_url = cleaned_url[:-1] 
        Names.append(cleaned_url)

# Print cleaned links
for cleaned_url in Names:
    if cleaned_url.isalpha():
        result = "".join([cleaned_url,".NS"])
        Final.append(result)
    elif cleaned_url.isnumeric():
        result = "".join([cleaned_url,".BO"])
        Final.append(result)

symbols = {item.split('.')[0]: item for item in Final}

time.sleep(3)
print("Stoking started")


result_df = pd.DataFrame()
# for name, symbol in symbols.items():
#     stock = yf.Ticker(symbol)
#     historical_data = stock.history(period="max")
#     if historical_data.empty:
#         print(f"No data available for {name} ({symbol})")
#         continue
    
#     # Ensure the Date column is in datetime format and sort the data in ascending order by date
#     historical_data.reset_index(inplace=True)
#     historical_data['Date'] = pd.to_datetime(historical_data['Date'])
#     historical_data = historical_data.sort_values(by='Date')
#     max_high = historical_data['High'].max()
#     max_high_date = historical_data['High'].idxmax()
    
    
#     # Calculate EMAs for the High column with periods of 50, 100, 150, 200, and 250 days
#     ema_periods = [50, 100, 150, 200, 250]
#     for period in ema_periods:
#         column_name = f"{period}_day_EMA_High"
#         historical_data[column_name] = historical_data['High'].ewm(span=period, adjust=False).mean()
    
#     # Remove columns Open, Low, Close, Volume, Dividends, Stock Splits, Capital Gains
#     columns_to_remove = ['Open', 'Low', 'Close', 'Volume','Capital Gains','Stock Splits','Dividends']
#     for col in columns_to_remove:
#         if col in historical_data.columns:
#             historical_data.drop(columns=[col], inplace=True)
    
#     # Add Stock Name column at the beginning
#     historical_data.insert(0, "Stock Name", name)
    
#     # Append the most recent data to the result DataFrame
#     current_data = historical_data.tail(1)
#     result_df = pd.concat([result_df, current_data])

# # Save the result DataFrame to a CSV file
# result_df.to_csv(f" 52 week high_{current_date}.csv", index=False)


# print("Data has been appended and saved to appended_data.csv")


for name, symbol in symbols.items():
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period="max")
    if historical_data.empty:
        print(f"No data available for {name} ({symbol})")
        continue
    
    # Ensure the Date column is in datetime format and sort the data in ascending order by date
    historical_data.reset_index(inplace=True)
    historical_data['Date'] = pd.to_datetime(historical_data['Date'])
    historical_data = historical_data.sort_values(by='Date')
    
    # Calculate the maximum high and its date
    max_high = historical_data['High'].max()
    max_high_date = historical_data.loc[historical_data['High'].idxmax(), 'Date']
    
    # Calculate EMAs for the High column with periods of 50, 100, 150, 200, and 250 days
    ema_periods = [50, 100, 150, 200, 250]
    for period in ema_periods:
        column_name = f"{period}_day_EMA_High"
        historical_data[column_name] = historical_data['High'].ewm(span=period, adjust=False).mean()
    
    # Remove columns Open, Low, Close, Volume, Dividends, Stock Splits, Capital Gains
    columns_to_remove = ['Open', 'Low', 'Close', 'Volume', 'Capital Gains', 'Stock Splits', 'Dividends']
    for col in columns_to_remove:
        if col in historical_data.columns:
            historical_data.drop(columns=[col], inplace=True)
    
    # Add Stock Name column at the beginning
    historical_data.insert(0, "Stock Name", name)
    
    # Add max_high and max_high_date columns
    historical_data['Max High'] = max_high
    historical_data['Max High Date'] = max_high_date
    
    # Append the most recent data to the result DataFrame
    current_data = historical_data.tail(1)
    result_df = pd.concat([result_df, current_data])

# Save the result DataFrame to a CSV file
result_df.to_csv(f"52_week_high_{current_date}.csv", index=False)

print("Data has been appended and saved to the CSV file.")









   

