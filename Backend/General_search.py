from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    # Replace with your actual database name.
    db = client['Campus'] 
    return db

def findAvailableRoom(db, groupSize, students):
    # Fetching all the dorms to loop through.
    dorms = db.rooms.find()
    for dorm in dorms:
        hall = dorm["dorm_name"]
        room_id = str(dorm["_id"])
        occupants = dorm.get("Occupants", [])
        size = dorm["size"]

        if len(occupants) + groupSize <= size:
            occupants.extend(students)
            # Update the room occupants in MongoDB.
            db.rooms.update_one({"_id": dorm["_id"]}, {"$set": {"Occupants": occupants}})
            return True, hall + " " + room_id
    return False, None

def printData(db):
    dorms = db.rooms.find()
    for dorm in dorms:
        print(dorm["dorm_name"], ":")
        print("  ", dorm["_id"], ":")
        print("    room size:", dorm["size"])
        print("    shared bathroom:", dorm["shared_bathroom"])
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

