from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    # Replace with your actual database name.
    db = client['Campus'] 
    return db

def findAvailableRoom(db, groupSize, students):
    # Query to find a room with empty occupants and sufficient size
    potential_room = db['Dorms_Rohan'].find_one({
        "Occupants": [],
        "Size": {"$gte": groupSize}
    })
    
    if potential_room:
        hall = potential_room["Dorm"]
        room_id = str(potential_room["_id"])
        
        # Update the room occupants in MongoDB.
        db['Dorms_Rohan'].update_one({"_id": potential_room["_id"]}, {"$set": {"Occupants": students}})
        return True, hall + " " + str(potential_room["RoomNum"])
    
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

students = ["John", "Bill"]
groupSize = len(students)

room_found, given_room = findAvailableRoom(db, groupSize, students)

if room_found:
    print("Room found:", given_room)
else:
    print("No suitable room found for the group.")

printData(db)





