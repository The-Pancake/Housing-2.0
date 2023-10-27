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

# Connect to database => "Campus" and collection => "Dorms_Daniel"
db = client["Campus"]["Dorms_Daniel"]

# Print everything out in collection using: 
# for doc in db.find():
#     print(doc)

Crockett = db.find_one()

# With this we have access the the data base 

