from pymongo import MongoClient
import copy
#General Near Search algorithm:
# Argurments:
#   grouplist: a list of the name of students in a group
#   campus: dictionary that has data of the campus dorms and info contain within them (json file converted in "main")
#In the case that General search and Ideal search fail to find a room for a group
#this algorithm splits the groups up and tries to find 2 rooms within the same building to assign
#the students to

def connect_to_db(uri):
    client = MongoClient(uri)
    db = client['Campus']  
    return db

def General_Near_Search(group_list, db):
    group_size = len(group_list)
    middle_index = group_size // 2
    group1 = group_list[:middle_index]
    group2 = group_list[middle_index:]
    room1_found = False
    room2_found = False

    # Querying all dorm rooms from the database
    dorms = db.rooms.find()
    for dorm in dorms:
        dorm_name = dorm["dorm_name"]
        room_id = str(dorm["_id"])
        occupants = dorm.get("Occupants", [])

        # Skip rooms that don't fit the group size or are already occupied
        if dorm["size"] != len(group1) or len(occupants) > 0:
            continue
        else:
            # Check if the room has a connected bathroom
            if dorm["shared_bathroom"] != False:
                connected_room = db.rooms.find_one({"_id": dorm["shared_bathroom"]})
                if not connected_room:
                    continue

                # Check if the connected room is suitable for the second group
                if connected_room["size"] == len(group2) and len(connected_room["Occupants"]) == 0:
                    # Update the Occupants of both rooms in the database
                    db.rooms.update_one({"_id": dorm["_id"]}, {"$set": {"Occupants": copy.deepcopy(group1)}})
                    db.rooms.update_one({"_id": connected_room["_id"]}, {"$set": {"Occupants": copy.deepcopy(group2)}})
                    return True
    return False

# Connection URI
uri = "mongodb+srv://housing20rcos:nQWnpyw4PsFk78eJ@housing2.elxx6hn.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
try:
    db = connect_to_db(uri)
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)
    exit()

group = ["Alice", "Bob", "Charlie", "David"]
if General_Near_Search(group, db):
    # Fetch the updated rooms and print them.
    rooms = db.rooms.find()
    for room in rooms:
        print(room)
else:
    print("did not find rooms for the group :(")

