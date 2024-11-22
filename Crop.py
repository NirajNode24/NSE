# import time
# import csv
# from playwright.async_api import async_playwright, TimeoutError
# from datetime import datetime

# current_time = datetime.now()


# async def run(playwright) -> None:
#     browser = await playwright.chromium.launch(headless=True)
#     context = await browser.new_context()
#     page = await context.new_page()
#     await page.goto("https://www.screener.in/screens/2232034/52-week-high-by-irshad/?sort=down+from+52w+high")

#     all_data = []

#     while True:
#         table = await page.query_selector("table.data-table.text-nowrap.striped.mark-visited")
#         rows = await table.query_selector_all("tr")

#         for row in rows:
#             cells = await row.query_selector_all("td")
#             if cells:  # Skip empty rows
#                 data = [await cell.inner_text() for cell in cells]
#                 all_data.append(data)

#         # Check if the "Next" button is present and clickable
#         try:
#             next_button = page.get_by_role("link", name="Next ")
#             if not await next_button.is_visible():
#                 break  # Exit if the "Next" button is not visible

#             await next_button.click()  # Click the "Next" button
#             await page.wait_for_load_state("networkidle")  # Wait for the page to load
#         except TimeoutError:
#             break  # Exit if the "Next" button click fails or the page doesn't load

#         time.sleep(2)  # Small delay to ensure data is fully loaded

#     # Define the CSV file columns
#     columns = ["S.No.", "Name", "CMP Rs.", "P/E", "Mar Cap Rs.Cr.", "Div Yld %", "NP Qtr Rs.Cr.", "Qtr Profit Var %", "Sales Qtr Rs.Cr.", "Qtr Sales Var %", "ROCE %", "Down %"]

#     # Write the data to a CSV file
#     with open('52 week high stocks'+ current_time, 'w', newline='', encoding='utf-8') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(columns)  # Write the header
#         csvwriter.writerows(all_data)  # Write the data

#     await context.close()
#     await browser.close()

# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)

# import asyncio
# asyncio.run(main())

# print("Data has been scraped and saved to scraped_data.csv")


import time
import csv
from playwright.async_api import async_playwright, TimeoutError
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  

async def run(playwright) -> None:
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.screener.in/screens/2232034/52-week-high-by-irshad/?sort=name&limit=25&order=asc")

    all_data = []

    while True:
        table = await page.query_selector("table.data-table.text-nowrap.striped.mark-visited")
        rows = await table.query_selector_all("tr")

        for row in rows:
            cells = await row.query_selector_all("td")
            if cells: 
                data = [await cell.inner_text() for cell in cells]
                all_data.append(data)

        try:
            next_button = page.get_by_role("link", name="Next ")
            if not await next_button.is_visible():
                break 

            await next_button.click() 
            await page.wait_for_load_state("networkidle")  
        except TimeoutError:
            break 

        time.sleep(2) 

    columns = [
        "S.No.", "Name", "CMP Rs.", "P/E", "Mar Cap Rs.Cr.", "Div Yld %",
        "NP Qtr Rs.Cr.", "Qtr Profit Var %", "Sales Qtr Rs.Cr.",
        "Qtr Sales Var %", "ROCE %", "Down %"
    ]

    file_name = f'52_week_high_stocks_{current_time}.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(columns) 
        csvwriter.writerows(all_data) 

    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

import asyncio
asyncio.run(main())

print("Data has been scraped and saved to a CSV file.")
