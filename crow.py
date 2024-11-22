

# import time
# from playwright.sync_api import Playwright, sync_playwright, TimeoutError

# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=True)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.screener.in/screens/2232034/52-week-high-by-irshad/?sort=down+from+52w+high")

#     all_data = []

#     while True:
#         table = page.query_selector("table.data-table.text-nowrap.striped.mark-visited")
#         rows = table.query_selector_all("tr")

#         for row in rows:
#             cells = row.query_selector_all("td")
#             if cells: 
#                 data = [cell.inner_text() for cell in cells]
#                 all_data.append(data)

#         try:
#             next_button = page.get_by_role("link", name="Next ")
#             if not next_button.is_visible():
#                 break 

#             next_button.click() 
#             page.wait_for_load_state("networkidle") 
#         except TimeoutError:
#             break 
#         time.sleep(2)

#     for data in all_data:
#         print(data)

#     context.close()
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)

