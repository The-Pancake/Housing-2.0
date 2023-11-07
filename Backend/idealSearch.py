from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    db = client['Campus'] 
    return db

def idealSearch(db, groupSize, preferred, students):
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


def printData(db):
    dorms = db['Dorms_Rohan'].find()
    for dorm in dorms:
        print(dorm["Dorm"], ":")
        print("  ", dorm["RoomNum"], ":")
        print("    room size:", dorm["Size"])
        print("    shared bathroom:", dorm["sharedBathroom"])
        print("    type:", dorm["type"])
        print("    occupants:")
        for occupant in dorm["Occupants"]:
            print("\t", occupant)

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()

preferences = ["Barton", "Hall", "Blitman", "Davison"]
students = ["Selena", "Nicky", "Beyonce"]
groupSize = len(students)

room_found, given_room = idealSearch(db, groupSize, preferences, students)

if room_found:
    print("Room found:", given_room)
else:
    print("No suitable room found for the group.")

printData(db)

