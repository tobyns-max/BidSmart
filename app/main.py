from fastapi import FastAPI
from app.scraping.scraper import scrape_sold_properties

# Create the FastAPI app
app = FastAPI()

# Simple home route to confirm the API is running
@app.get("/")
def root():
    return {"message": "BidSmart API is live"}

# New route: scrape sold property data via query parameters
@app.get("/scrape")
def get_scraped_data(suburb: str, state: str = "nsw"):
    """
    API endpoint to scrape sold property data from realestate.com.au.
    Example: /scrape?suburb=newtown&state=nsw
    """
    comps = scrape_sold_properties(suburb=suburb, state=state)
    return {"results": comps}