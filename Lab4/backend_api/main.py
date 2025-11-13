from fastapi import FastAPI
from data_layer.donation_model import create_donation, list_donations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SaveBite API is running!"}

@app.post("/donations")
def add_donation(donor_name: str, food_type: str, quantity: int, pickup_time: str):
    donation = create_donation(donor_name, food_type, quantity, pickup_time)
    return {"status": "Donation created", "donation": donation}

@app.get("/donations")
def get_donations():
    return list_donations()
