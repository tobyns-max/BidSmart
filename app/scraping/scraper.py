import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def scrape_sold_properties(suburb: str, state: str) -> List[Dict]:
    formatted_suburb = suburb.replace(' ', '+').lower()
    url = f"https://www.realestate.com.au/sold/in-{formatted_suburb}%2c+{state}/list-1"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url} - Status {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    listings = soup.select("div.residential-card__content-wrapper")
    for listing in listings:
        try:
            price_text = listing.select_one("span.property-price").text.strip()
            price = int(price_text.replace('$', '').replace(',', '').strip())

            address = listing.select_one("a.residential-card__details-link span").text.strip()

            beds_tag = listing.select("li[aria-label*='bedrooms'] p")
            beds = int(beds_tag[0].text.strip()) if beds_tag else None

            baths_tag = listing.select("li[aria-label*='bathrooms'] p")
            baths = int(baths_tag[0].text.strip()) if baths_tag else None

            cars_tag = listing.select("li[aria-label*='car spaces'] p")
            car_spaces = int(cars_tag[0].text.strip()) if cars_tag else None

            building_size_tag = listing.select("li[aria-label*='building size'] p")
            land_size = building_size_tag[0].text.strip() if building_size_tag else None

            property_type_tag = listing.select("ul.residential-card__primary > p")
            property_type = property_type_tag[-1].text.strip() if property_type_tag else None

            sold_span = listing.find("span", string=lambda t: t and "Sold on" in t)
            sold_date = sold_span.text.replace("Sold on", "").strip() if sold_span else None

            results.append({
                "address": address,
                "sold_price": price,
                "beds": beds,
                "baths": baths,
                "car_spaces": car_spaces,
                "building_size": land_size,
                "property_type": property_type,
                "sold_date": sold_date
            })

        except Exception as e:
            continue  # Skip listings that fail parsing

    return results