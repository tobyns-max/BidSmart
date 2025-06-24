import requests
from bs4 import BeautifulSoup

def scrape_sold_properties(suburb: str, state: str):
    # Construct the URL for the sold listings page based on suburb and state
    url = f"https://www.realestate.com.au/sold/in-{suburb}%2c+{state}/list-1"

    # Add headers to mimic a real browser
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        )
    }

    # Send the GET request with headers
    response = requests.get(url, headers=headers)
    
    print(response.text[:2000])  # print first 2000 chars of the page HTML

    # Handle rate-limiting (HTTP 429)
    if response.status_code == 429:
        print("⚠️ Rate limited by the site. Try again later.")
        return []

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url} - Status {response.status_code}")

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    # Find each property listing on the page
    listings = soup.find_all("div", class_="residential-card__content-wrapper")

    for listing in listings:
        try:
            # Extract the property address
            address = listing.find("h2", class_="residential-card__address-heading").get_text(strip=True)

            # Extract the price
            price_text = listing.find("span", class_="property-price").get_text(strip=True)
            price = int(price_text.replace("$", "").replace(",", ""))

            # Extract features like beds, baths, cars
            features = listing.find_all("li", class_="styles__Li-sc-xhfhyt-0")
            beds = int(features[0].get_text(strip=True)) if len(features) > 0 else None
            baths = int(features[1].get_text(strip=True)) if len(features) > 1 else None
            cars = int(features[2].get_text(strip=True)) if len(features) > 2 else None

            # Optional: building size
            size_elem = next((li for li in features if "m²" in li.get_text()), None)
            size = size_elem.get_text(strip=True) if size_elem else None

            # Append to results
            results.append({
                "address": address,
                "price": price,
                "bedrooms": beds,
                "bathrooms": baths,
                "car_spaces": cars,
                "size": size
            })

        except Exception as e:
            print(f"⚠️ Skipped a listing due to error: {e}")
            continue

    return results
