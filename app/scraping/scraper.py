from playwright.sync_api import sync_playwright

def scrape_sold_properties(suburb: str, state: str):
    url = f"https://www.realestate.com.au/sold/in-{suburb},+{state}/list-1"
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"[INFO] Navigating to: {url}")
        page.goto(url, timeout=60000)

        # Wait for property cards to load
        page.wait_for_selector(".residential-card__content-wrapper", timeout=15000)

        cards = page.query_selector_all(".residential-card__content-wrapper")

        for card in cards:
            try:
                price = card.query_selector(".property-price").inner_text()
                address = card.query_selector(".residential-card__address-heading").inner_text()
                sold_on = card.inner_text().split("Sold on ")[-1].split("\n")[0]
                beds = card.query_selector('li[aria-label*="bedroom"]').inner_text()
                baths = card.query_selector('li[aria-label*="bathroom"]').inner_text()
                cars = card.query_selector('li[aria-label*="car space"]').inner_text()
                
                results.append({
                    "price": price,
                    "address": address,
                    "sold_on": sold_on,
                    "beds": beds,
                    "baths": baths,
                    "cars": cars
                })
            except Exception as e:
                print("[WARNING] Failed to parse card:", e)
        
        browser.close()
    return results

