 # Import the FastAPI class from the fastapi package
# This is the main tool used to define and manage your API
from fastapi import FastAPI

# Create an instance of the FastAPI class
# This 'app' object is what the server will use to route requests
app = FastAPI()

# Define a route (also called an endpoint) that handles GET requests to "/"
# In web terms, this is the homepage or root path
@app.get("/")
def root():
    # This is the function that runs when someone visits "/"
    # It returns a dictionary, which FastAPI automatically converts to JSON
    return {"message": "BidSmart API is live"}

