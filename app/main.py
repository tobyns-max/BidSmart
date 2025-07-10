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
def get_scraped_data(suburb: str, state: str):
    return {"results": [{"address": "123 Test St", "price": "$1,000,000"}]}
