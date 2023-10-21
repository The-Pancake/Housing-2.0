from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["Campus"]["Dorms"]

query = {}

result = db.find(query)

for something in result:
    print(something)

db.insert_one(
    {
     "_id": 6969696969,
     "Dorm": "Blitman", 
     "RoomNum": 104, 
     "Size": 2, 
     "sharedBathroom": True, 
     "sharedRoom": 2, 
     "type": "Freshman", 
     "Occupants": ["Rachael", "Michelle"]
    }
    )