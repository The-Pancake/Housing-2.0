from pymongo import MongoClient

def connect_to_db(uri):
    client = MongoClient(uri)
    db = client['Campus'] 
    return db

def idealSearch(db, groupSize, preferred, students):
    for pref in preferred:
        # Query to find rooms with enough space
        rooms = db.rooms.find({"dorm_name": pref, "size": {"$gte": groupSize + len(students)}})

        for room in rooms:
            occupants = room.get("Occupants", [])
            
            if len(occupants) + groupSize <= room["size"]:
                # Add students to occupants
                occupants.extend(students)
                
                # Update the room occupants in MongoDB
                db.rooms.update_one({"_id": room["_id"]}, {"$set": {"Occupants": occupants}})
                
                return True, pref + " " + str(room["_id"])
                
            elif len(occupants) == 0 and groupSize <= room["size"]:
                # Add as many students as the room can take
                occupants.extend(students[:room["size"]])
                
                # Update the room occupants in MongoDB
                db.rooms.update_one({"_id": room["_id"]}, {"$set": {"Occupants": occupants}})
                
                return True, pref + " " + str(room["_id"])
                
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

preferred1 = ["Davison"]
students = ["kellie", "Becky"]
groupSize = len(students)

room_found, given_room = idealSearch(db, groupSize, preferred1, students)

if room_found:
    print("Room found:", given_room)
else:
    print("No suitable room found for the group.")

printData(db)


