
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://dporter:12345aA!@cluster0.s9ulfeb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.CMA
print(db)
collection = client.Exhibition
print(collection)
# Send a ping to confirm a successful connection

test = [
  {
    "_id": "620eaf735a516a0f586af39c",
    "index": 0,
    "name": "Ruby Spears",
    "gender": "female",
    "company": "BIFLEX",
    "email": "rubyspears@biflex.com"
  }
]

try:
    client.admin.command('ping')
    collection.insert_one(test)

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
