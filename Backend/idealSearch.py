from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    db = client['Campus'] 
    return db

def searchIdeal(db, groupSize, preferred, students):
    for pref in preferred:
        # Query to find rooms with enough space and empty Occupants array
        room = db['Dorms_Rohan'].find_one({
            "Dorm": pref, 
            "Size": {"$gte": groupSize}, 
            "Occupants": []
        })

        if room:
            # Add students to occupants
            occupants = students
            
            # Update the room occupants in MongoDB
            db['Dorms_Rohan'].update_one({"_id": room["_id"]}, {"$set": {"Occupants": occupants}})
            return True, f"{pref} Room {room['RoomNum']}"  # Return the dorm name and room number
    return False, None

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()




