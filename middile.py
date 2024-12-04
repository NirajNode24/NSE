from playwright.sync_api import sync_playwright, TimeoutError

base_url = "https://www.screener.in"
company_base_url = "https://www.screener.in/company/"
Names = []

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

# Cleaning up the extracted URLs
for link in all_links:
    if link.startswith(company_base_url):
        cleaned_url = link[len(company_base_url):]
        if cleaned_url.endswith("/consolidated/"):
            cleaned_url = cleaned_url[:-len("/consolidated/")]
        elif cleaned_url.endswith("/"):
            cleaned_url = cleaned_url[:-1]
        if cleaned_url.isalpha():
            cleaned_url+ "NS"
        if cleaned_url.isnumeric():
            cleaned_url + "BO"    
        Names.append(cleaned_url)

# Print cleaned links
for cleaned_url in Names:
    print(cleaned_url)
