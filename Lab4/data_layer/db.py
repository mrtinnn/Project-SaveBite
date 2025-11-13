from pymongo import MongoClient

# Change this if your MongoDB runs elsewhere
client = MongoClient("mongodb://localhost:27017/")

db = client["savebite_db"]   # database name
