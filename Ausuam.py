# import yfinance as yf
# import pandas as pd

# output_file = 'formatted_stock_dma.csv'

# Final =['532067.BSE', 'ABREL.NS', '542012.BSE', 'AARON.NS', '539528.BSE', '512165.BSE', '531525.BSE', 'ADFFOODS.NS', 'BIRLAMONEY.NS', 'ABSLAMC.NS', 'AEGISLOG.NS', 'AFFLE.NS', 'AGARIND.NS', 'AJMERA.NS', '535916.BSE', '543225.BSE', '506597.BSE', 'AMIORG.NS', 'ANANDRATHI.NS', 'ANIKINDS.NS', 'ARIES.NS', '531381.BSE', '526443.BSE', 'ARVSMART.NS', '543766.BSE', 'ASKAUTOLTD.NS', 'ASALCBR.NS', '538713.BSE', 'AVALON.NS', 'AVONMORE.NS', 'AYMSYNTEX.NS', 'BAJAJHLDNG.NS', 'BANCOINDIA.NS', '539399.BSE', 'BFINVEST.NS', 'BHARTIHEXA.NS', 'BIL.NS', '526709.BSE', 'BSE.NS', 'CDSL.NS', 'CAMS.NS', 'CAPACITE.NS', 'CARERATING.NS', 'CARTRADE.NS', 'CCL.NS', '538734.BSE', 'CHOICEIN.NS', '519477.BSE', '513353.BSE', 
# 'COFORGE.NS', 'DEEPINDS.NS', '504240.BSE', 'DEVIT.NS', 'DHRUV.NS', 'DHUNINV.NS', 'DIVISLAB.NS', 'DIXON.NS', 'DJML.NS', 'DLF.NS', 'DODLA.NS', '526783.BSE', 'DYCL.NS', 'DYNPRO.NS', '512008.BSE', '531364.BSE', 'EMCURE.NS', '538882.BSE', 'EMKAY.NS', 'EMUDHRA.NS', 'ENTERO.NS', 'EPIGRAL.NS', 'ERIS.NS', 'ETHOSLTD.NS', 'EIFFL.NS', 'EKC.NS', 'EXCEL.NS', 'FEDERALBNK.NS', 'FIEMIND.NS', 'FINEORG.NS', 'FSL.NS', '522017.BSE', '522195.BSE', 'GANESHHOUC.NS', 'GANECOS.NS', 'GRWRHITECH.NS', 'GARFIBRES.NS', 'GEECEE.NS', 'GENESYS.NS', 'GENUSPOWER.NS', 'GODAVARIB.NS', 'GOKEX.NS', '540062.BSE', '539854.BSE', 'HDFCAMC.NS', 'HDFCLIFE.NS', 'HIRECT.NS', 'ICICIPRULI.NS', 'ISEC.NS', 'ICRA.NS', 'IGARASHI.NS', 
# 'INDHOTEL.NS', '540954.BSE', 'IITL.NS', '501298.BSE', 'INDOTECH.NS', '531889.BSE', 'IONEXCHANG.NS', 'IRIS.NS', 'IZMO.NS', 'JGCHEM.NS', 'JAGSNPHARM.NS', 'JASH.NS', '524592.BSE', 'JINDRILL.NS']



# for name in Final:
#     try:
#         stock = yf.Ticker(name)
#         info = stock.info
#         if 'regularMarketPrice' not in info or info['regularMarketPrice'] is None:
#             print(f"name {name} appears invalid or delisted. Logging and skipping...")
#             with open(skipped_names_file, 'a') as log_file:
#                 log_file.write(f"{name} ({name}) - Invalid or delisted\n")
#             continue

#         historical_data = stock.history(period="1y")  # Last 1 year
#         if historical_data.empty:
#             print(f"No data available for {name}. Logging and skipping...")
#             with open(skipped_names_file, 'a') as log_file:
#                 log_file.write(f"{name} ({name}) - No historical data\n")
#             continue

#         historical_data = historical_data.sort_index(ascending=False)  # Sort in descending order
#         close_data = historical_data['Close']  # Select only the 'Close' column

#         close_data_25_days = close_data[::25]

#         # Prepare DAYS columns
#         days_dict = {
#             f'DAYS_{i*25}': [close_data_25_days.iloc[i]] if i < len(close_data_25_days) else [None]
#             for i in range(len(close_data_25_days))
#         }

#         stock_df = pd.DataFrame(days_dict)
#         stock_df.insert(0, 'Name', name)

#         # Append to the output CSV file
#         with open(output_file, 'a') as f:
#             stock_df.to_csv(f, header=False, index=False)
#     except Exception as e:
#         print(f"Error fetching data for {name} ({name}): {e}")
#         with open(skipped_names_file, 'a') as log_file:
#             log_file.write(f"{name} ({name}) - {e}\n")

# print(f"The CSV file '{output_file}' has been updated successfully.")
# print(f"Skipped names have been logged to '{skipped_names_file}'.")



  


import yfinance as yf

# List of stock symbols
symbo = ['532067.BSE', 'ABREL.NS', '542012.BSE', 'AARON.NS', '539528.BSE', '512165.BSE', '531525.BSE', 'ADFFOODS.NS',
         'BIRLAMONEY.NS', 'ABSLAMC.NS', 'AEGISLOG.NS', 'AFFLE.NS', 'AGARIND.NS', 'AJMERA.NS', '535916.BSE', '543225.BSE',
         '506597.BSE', 'AMIORG.NS', 'ANANDRATHI.NS', 'ANIKINDS.NS', 'ARIES.NS', '531381.BSE', '526443.BSE', 'ARVSMART.NS',
         '543766.BSE', 'ASKAUTOLTD.NS', 'ASALCBR.NS', '538713.BSE', 'AVALON.NS', 'AVONMORE.NS', 'AYMSYNTEX.NS', 'BAJAJHLDNG.NS',
         'BANCOINDIA.NS', '539399.BSE', 'BFINVEST.NS', 'BHARTIHEXA.NS', 'BIL.NS', '526709.BSE', 'BSE.NS', 'CDSL.NS', 'CAMS.NS',
         'CAPACITE.NS', 'CARERATING.NS', 'CARTRADE.NS', 'CCL.NS', '538734.BSE', 'CHOICEIN.NS', '519477.BSE', '513353.BSE',
         'COFORGE.NS', 'DEEPINDS.NS', '504240.BSE', 'DEVIT.NS', 'DHRUV.NS', 'DHUNINV.NS', 'DIVISLAB.NS', 'DIXON.NS', 'DJML.NS',
         'DLF.NS', 'DODLA.NS', '526783.BSE', 'DYCL.NS', 'DYNPRO.NS', '512008.BSE', '531364.BSE', 'EMCURE.NS', '538882.BSE',
         'EMKAY.NS', 'EMUDHRA.NS', 'ENTERO.NS', 'EPIGRAL.NS', 'ERIS.NS', 'ETHOSLTD.NS', 'EIFFL.NS', 'EKC.NS', 'EXCEL.NS',
         'FEDERALBNK.NS', 'FIEMIND.NS', 'FINEORG.NS', 'FSL.NS', '522017.BSE', '522195.BSE', 'GANESHHOUC.NS', 'GANECOS.NS',
         'GRWRHITECH.NS', 'GARFIBRES.NS', 'GEECEE.NS', 'GENESYS.NS', 'GENUSPOWER.NS', 'GODAVARIB.NS', 'GOKEX.NS', '540062.BSE',
         '539854.BSE', 'HDFCAMC.NS', 'HDFCLIFE.NS', 'HIRECT.NS', 'ICICIPRULI.NS', 'ISEC.NS', 'ICRA.NS', 'IGARASHI.NS',
         'INDHOTEL.NS', '540954.BSE', 'IITL.NS', '501298.BSE', 'INDOTECH.NS', '531889.BSE', 'IONEXCHANG.NS', 'IRIS.NS',
         'IZMO.NS', 'JGCHEM.NS', 'JAGSNPHARM.NS', 'JASH.NS', '524592.BSE', 'JINDRILL.NS']


symbols = {}
for symbol in symbo:
    # Extract the stock name (without extension)
    stock_name = symbol[:-4]  # Assuming extension is always 4 characters (e.g., '.NS', '.BSE')
    symbols[stock_name] = symbol

print(symbols)
historical_data = {}

for stock in symbols:
    try:
        print(stock)
        stock_data = yf.Ticker(stock).history(period="1y")
        historical_data[stock] = stock_data
        print(f"Data fetched for {stock}")
    except Exception as e:
        print(f"Failed to fetch data for {stock}: {e}")

# Example: Access data for a specific stock (e.g., '532067.BSE')
print(historical_data['532067.BSE'])
