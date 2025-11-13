from datetime import datetime
from .db import db

donations_collection = db["donations"]

def create_donation(donor_name, food_type, quantity, pickup_time):
    donation = {
        "donor_name": donor_name,
        "food_type": food_type,
        "quantity": quantity,
        "pickup_time": pickup_time,
        "created_at": datetime.now(),
        "status": "available"
    }
    donations_collection.insert_one(donation)
    return donation

def list_donations():
    return list(donations_collection.find())
